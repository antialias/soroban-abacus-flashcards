#!/usr/bin/env python3

import argparse
import json
import yaml
import random
import subprocess
import sys
import os
from pathlib import Path

def load_config(config_path):
    """Load configuration from JSON or YAML file."""
    with open(config_path, 'r') as f:
        if config_path.endswith('.yaml') or config_path.endswith('.yml'):
            return yaml.safe_load(f)
        else:
            return json.load(f)

def parse_range(range_str, step=1):
    """Parse a range string like '0-99' or a comma-separated list.
    
    Examples:
        '0-10' with step=1 -> [0, 1, 2, ..., 10]
        '0-10' with step=2 -> [0, 2, 4, 6, 8, 10]
        '0-20' with step=5 -> [0, 5, 10, 15, 20]
        '1,2,5,10' -> [1, 2, 5, 10] (step ignored for lists)
    """
    numbers = []
    if ',' in range_str:
        # Comma-separated list (step is ignored)
        for part in range_str.split(','):
            part = part.strip()
            if '-' in part:
                start, end = map(int, part.split('-'))
                numbers.extend(range(start, end + 1, step))
            else:
                numbers.append(int(part))
    elif '-' in range_str:
        # Range with optional step
        start, end = map(int, range_str.split('-'))
        numbers = list(range(start, end + 1, step))
    else:
        # Single number
        numbers = [int(range_str)]
    return numbers

def generate_typst_file(numbers, config, output_path):
    """Generate a Typst file with the specified configuration."""
    
    # Convert Python list to Typst array syntax
    numbers_str = '(' + ', '.join(str(n) for n in numbers) + ',)'
    
    # Build the Typst document
    # Use relative path from project root where temp file is created
    typst_content = f'''
#import "templates/flashcards.typ": generate-flashcards

#generate-flashcards(
  {numbers_str},
  cards-per-page: {config.get('cards_per_page', 6)},
  paper-size: "{config.get('paper_size', 'us-letter')}",
  orientation: "{config.get('orientation', 'portrait')}",
  margins: (
    top: {config.get('margins', {}).get('top', '0.5in')},
    bottom: {config.get('margins', {}).get('bottom', '0.5in')},
    left: {config.get('margins', {}).get('left', '0.5in')},
    right: {config.get('margins', {}).get('right', '0.5in')}
  ),
  gutter: {config.get('gutter', '5mm')},
  show-cut-marks: {str(config.get('show_cut_marks', False)).lower()},
  show-registration: {str(config.get('show_registration', False)).lower()},
  font-family: "{config.get('font_family', 'DejaVu Sans')}",
  font-size: {config.get('font_size', '48pt')},
  columns: {config.get('columns', 'auto')},
  show-empty-columns: {str(config.get('show_empty_columns', False)).lower()},
  hide-inactive-beads: {str(config.get('hide_inactive_beads', False)).lower()},
  bead-shape: "{config.get('bead_shape', 'diamond')}",
  color-scheme: "{config.get('color_scheme', 'monochrome')}",
  colored-numerals: {str(config.get('colored_numerals', False)).lower()},
  scale-factor: {config.get('scale_factor', 0.9)}
)
'''
    
    with open(output_path, 'w') as f:
        f.write(typst_content)

def main():
    parser = argparse.ArgumentParser(description='Generate Soroban flashcards PDF')
    parser.add_argument('--config', '-c', type=str, help='Configuration file (JSON or YAML)')
    parser.add_argument('--range', '-r', type=str, help='Number range (e.g., "0-99") or list (e.g., "1,2,5,10")')
    parser.add_argument('--step', '-s', type=int, default=1, help='Step/increment for ranges (e.g., 2 for counting by 2s)')
    parser.add_argument('--cards-per-page', type=int, default=6, help='Cards per page (default: 6)')
    parser.add_argument('--paper-size', type=str, default='us-letter', help='Paper size (default: us-letter)')
    parser.add_argument('--orientation', type=str, choices=['portrait', 'landscape'], default='portrait', help='Page orientation')
    parser.add_argument('--margins', type=str, help='Margins in format "top,right,bottom,left" (e.g., "0.5in,0.5in,0.5in,0.5in")')
    parser.add_argument('--gutter', type=str, default='5mm', help='Space between cards (default: 5mm)')
    parser.add_argument('--shuffle', action='store_true', help='Shuffle the numbers')
    parser.add_argument('--seed', type=int, help='Random seed for shuffle (for deterministic builds)')
    parser.add_argument('--cut-marks', action='store_true', help='Show cut marks')
    parser.add_argument('--registration', action='store_true', help='Show registration marks')
    parser.add_argument('--font-family', type=str, default='DejaVu Sans', help='Font family')
    parser.add_argument('--font-size', type=str, default='48pt', help='Font size')
    parser.add_argument('--columns', type=str, default='auto', help='Number of soroban columns (auto or integer)')
    parser.add_argument('--show-empty-columns', action='store_true', help='Show leading empty columns')
    parser.add_argument('--hide-inactive-beads', action='store_true', help='Hide inactive beads (only show active ones)')
    parser.add_argument('--bead-shape', type=str, choices=['diamond', 'circle', 'square'], default='diamond', help='Bead shape (default: diamond)')
    parser.add_argument('--color-scheme', type=str, choices=['monochrome', 'place-value', 'heaven-earth', 'alternating'], default='monochrome', help='Color scheme (default: monochrome)')
    parser.add_argument('--colored-numerals', action='store_true', help='Color the numerals to match the bead color scheme')
    parser.add_argument('--scale-factor', type=float, default=0.9, help='Manual scale adjustment (0.1 to 1.0, default: 0.9)')
    parser.add_argument('--output', '-o', type=str, default='out/flashcards.pdf', help='Output PDF path')
    parser.add_argument('--linearize', action='store_true', default=True, help='Create linearized PDF (default: True)')
    parser.add_argument('--font-path', type=str, help='Path to fonts directory')
    
    args = parser.parse_args()
    
    # Load config file if provided
    config = {}
    if args.config:
        config = load_config(args.config)
    
    # Override config with command-line arguments
    step = args.step or config.get('step', 1)
    if args.range:
        numbers = parse_range(args.range, step)
    elif 'range' in config:
        numbers = parse_range(config['range'], step)
    elif 'numbers' in config:
        numbers = config['numbers']
    else:
        # Default to 0-9
        numbers = list(range(0, 10, step))
    
    # Apply shuffle if requested
    if args.shuffle or config.get('shuffle', False):
        seed = args.seed or config.get('seed')
        if seed is not None:
            random.seed(seed)
        random.shuffle(numbers)
    
    # Build final configuration
    final_config = {
        'cards_per_page': args.cards_per_page or config.get('cards_per_page', 6),
        'paper_size': args.paper_size or config.get('paper_size', 'us-letter'),
        'orientation': args.orientation or config.get('orientation', 'portrait'),
        'gutter': args.gutter or config.get('gutter', '5mm'),
        'show_cut_marks': args.cut_marks or config.get('show_cut_marks', False),
        'show_registration': args.registration or config.get('show_registration', False),
        'font_family': args.font_family or config.get('font_family', 'DejaVu Sans'),
        'font_size': args.font_size or config.get('font_size', '48pt'),
        'show_empty_columns': args.show_empty_columns or config.get('show_empty_columns', False),
        'hide_inactive_beads': args.hide_inactive_beads or config.get('hide_inactive_beads', False),
        'bead_shape': args.bead_shape if args.bead_shape != 'diamond' else config.get('bead_shape', 'diamond'),
        'color_scheme': args.color_scheme if args.color_scheme != 'monochrome' else config.get('color_scheme', 'monochrome'),
        'colored_numerals': args.colored_numerals or config.get('colored_numerals', False),
        'scale_factor': args.scale_factor if args.scale_factor != 0.9 else config.get('scale_factor', 0.9),
    }
    
    # Handle margins
    if args.margins:
        parts = args.margins.split(',')
        if len(parts) == 4:
            final_config['margins'] = {
                'top': parts[0],
                'right': parts[1],
                'bottom': parts[2],
                'left': parts[3]
            }
    elif 'margins' in config:
        final_config['margins'] = config['margins']
    else:
        final_config['margins'] = {
            'top': '0.5in',
            'right': '0.5in',
            'bottom': '0.5in',
            'left': '0.5in'
        }
    
    # Handle columns
    if args.columns != 'auto':
        try:
            final_config['columns'] = int(args.columns)
        except ValueError:
            final_config['columns'] = 'auto'
    else:
        final_config['columns'] = config.get('columns', 'auto')
    
    # Create output directory
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Generate temporary Typst file in project root
    project_root = Path(__file__).parent.parent
    temp_typst = project_root / 'temp_flashcards.typ'
    generate_typst_file(numbers, final_config, temp_typst)
    
    # Set up font path if provided
    font_args = []
    if args.font_path:
        font_args = ['--font-path', args.font_path]
    elif os.path.exists('fonts'):
        font_args = ['--font-path', 'fonts']
    
    # Compile with Typst
    print(f"Generating flashcards for {len(numbers)} numbers...")
    try:
        # Run typst from project root directory
        project_root = Path(__file__).parent.parent
        result = subprocess.run(
            ['typst', 'compile'] + font_args + [str(temp_typst), str(output_path)],
            capture_output=True,
            text=True,
            cwd=str(project_root)
        )
        
        if result.returncode != 0:
            print(f"Error compiling Typst document:", file=sys.stderr)
            print(result.stderr, file=sys.stderr)
            sys.exit(1)
        
        print(f"Generated: {output_path}")
        
        # Clean up temp file
        temp_typst.unlink()
        
        # Add duplex printing hints and linearize if requested
        if args.linearize:
            linearized_path = output_path.parent / f"{output_path.stem}_linear{output_path.suffix}"
            print(f"Linearizing PDF with duplex hints...")
            
            # Use qpdf to add duplex hints and linearize
            # Note: --pages option preserves page order for duplex
            result = subprocess.run(
                ['qpdf', '--linearize', 
                 '--object-streams=preserve',
                 str(output_path), str(linearized_path)],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"Linearized: {linearized_path}")
            else:
                print(f"Warning: Failed to linearize PDF: {result.stderr}", file=sys.stderr)
        
        # Run basic PDF validation
        print("Validating PDF...")
        result = subprocess.run(
            ['qpdf', '--check', str(output_path)],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("PDF validation passed")
        else:
            print(f"Warning: PDF validation issues: {result.stderr}", file=sys.stderr)
            
    except FileNotFoundError as e:
        if 'typst' in str(e):
            print("Error: typst command not found. Please install Typst first.", file=sys.stderr)
            print("Visit: https://github.com/typst/typst", file=sys.stderr)
        elif 'qpdf' in str(e):
            print("Warning: qpdf command not found. Skipping linearization and validation.", file=sys.stderr)
            print("Install with: brew install qpdf", file=sys.stderr)
        else:
            raise
        sys.exit(1)

if __name__ == '__main__':
    main()