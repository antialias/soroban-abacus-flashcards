#!/usr/bin/env python3
"""
Generate example PNG images for the README
Converts PDFs to PNGs using ImageMagick or Ghostscript
"""

import subprocess
import os
from pathlib import Path
import tempfile

def generate_example_pdfs():
    """Generate various example PDFs to convert to PNG"""
    examples = [
        # Basic examples
        {
            'name': 'basic-7',
            'args': ['--range', '7-7', '--cards-per-page', '1'],
            'desc': 'Number 7 on soroban'
        },
        {
            'name': 'basic-123',
            'args': ['--range', '123-123', '--cards-per-page', '1'],
            'desc': 'Number 123 on soroban'
        },
        
        # Color schemes
        {
            'name': 'place-value-456',
            'args': ['--range', '456-456', '--cards-per-page', '1', '--color-scheme', 'place-value', '--colored-numerals'],
            'desc': 'Place-value coloring'
        },
        {
            'name': 'heaven-earth-78',
            'args': ['--range', '78-78', '--cards-per-page', '1', '--color-scheme', 'heaven-earth', '--colored-numerals'],
            'desc': 'Heaven-earth coloring'
        },
        
        # Bead shapes
        {
            'name': 'diamond-25',
            'args': ['--range', '25-25', '--cards-per-page', '1', '--bead-shape', 'diamond'],
            'desc': 'Diamond beads (realistic)'
        },
        {
            'name': 'circle-25',
            'args': ['--range', '25-25', '--cards-per-page', '1', '--bead-shape', 'circle'],
            'desc': 'Circle beads'
        },
        {
            'name': 'square-25',
            'args': ['--range', '25-25', '--cards-per-page', '1', '--bead-shape', 'square'],
            'desc': 'Square beads'
        },
        
        # Grid layouts
        {
            'name': 'grid-6',
            'args': ['--range', '0-5', '--cards-per-page', '6'],
            'desc': '6 cards per page'
        },
        {
            'name': 'grid-12',
            'args': ['--range', '0-11', '--cards-per-page', '12'],
            'desc': '12 cards per page'
        },
        
        # Skip counting
        {
            'name': 'skip-5s',
            'args': ['--range', '0-30', '--step', '5', '--cards-per-page', '6'],
            'desc': 'Counting by 5s'
        },
        
        # Hide inactive
        {
            'name': 'minimal-42',
            'args': ['--range', '42-42', '--cards-per-page', '1', '--hide-inactive-beads'],
            'desc': 'Hidden inactive beads'
        },
        
        # Cutting guides
        {
            'name': 'cutting-guides',
            'args': ['--range', '10-15', '--cards-per-page', '6', '--cut-marks'],
            'desc': 'With cutting guides'
        },
    ]
    
    return examples

def pdf_to_png(pdf_path, png_path, dpi=150, page=1):
    """Convert PDF to PNG using various methods"""
    
    # Method 1: Try pdftoppm (usually available on Unix systems)
    try:
        result = subprocess.run([
            'pdftoppm',
            '-png',
            '-f', str(page),
            '-l', str(page),
            '-r', str(dpi),
            '-singlefile',
            pdf_path,
            png_path.replace('.png', '')
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            # pdftoppm adds -1.png suffix, rename it
            temp_file = png_path.replace('.png', '-1.png')
            if os.path.exists(temp_file):
                os.rename(temp_file, png_path)
            return True
    except FileNotFoundError:
        pass
    
    # Method 2: Try ImageMagick convert
    try:
        result = subprocess.run([
            'convert',
            '-density', str(dpi),
            f'{pdf_path}[{page-1}]',  # ImageMagick uses 0-based indexing
            '-trim',
            '-bordercolor', 'white',
            '-border', '20x20',
            png_path
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            return True
    except FileNotFoundError:
        pass
    
    # Method 3: Try Ghostscript directly
    try:
        result = subprocess.run([
            'gs',
            '-dNOPAUSE',
            '-dBATCH',
            '-sDEVICE=png16m',
            f'-r{dpi}',
            f'-dFirstPage={page}',
            f'-dLastPage={page}',
            f'-sOutputFile={png_path}',
            pdf_path
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            return True
    except FileNotFoundError:
        pass
    
    # Method 4: Try sips (macOS)
    try:
        # First convert PDF to temporary format
        with tempfile.NamedTemporaryFile(suffix='.png') as tmp:
            result = subprocess.run([
                'sips',
                '-s', 'format', 'png',
                '--out', tmp.name,
                pdf_path
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                # Copy to final location
                subprocess.run(['cp', tmp.name, png_path])
                return True
    except FileNotFoundError:
        pass
    
    return False

def main():
    """Generate example images for README"""
    
    # Create output directories
    project_root = Path(__file__).parent.parent
    images_dir = project_root / 'docs' / 'images'
    images_dir.mkdir(parents=True, exist_ok=True)
    
    temp_dir = project_root / 'out' / 'examples'
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    examples = generate_example_pdfs()
    
    # Check if we have a PDF to PNG converter available
    converters = []
    for cmd in ['pdftoppm', 'convert', 'gs']:
        if subprocess.run(['which', cmd], capture_output=True).returncode == 0:
            converters.append(cmd)
    
    if not converters:
        print("ERROR: No PDF to PNG converter found. Please install one of:")
        print("  - poppler-utils (for pdftoppm)")
        print("  - imagemagick (for convert)")
        print("  - ghostscript (for gs)")
        print("\nOn Ubuntu/Debian: sudo apt-get install poppler-utils")
        print("On macOS: brew install poppler")
        return 1
    
    print(f"Using PDF converters: {', '.join(converters)}")
    print("Generating example images...")
    
    failed = []
    for example in examples:
        print(f"  - {example['name']}: {example['desc']}")
        
        # Generate PDF
        pdf_path = temp_dir / f"{example['name']}.pdf"
        cmd = [
            'python3',
            str(project_root / 'src' / 'generate.py'),
            '--output', str(pdf_path)
        ] + example['args']
        
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(project_root))
        
        if result.returncode != 0:
            print(f"    ERROR generating PDF: {result.stderr}")
            continue
        
        # Convert front page to PNG
        front_png = images_dir / f"{example['name']}-front.png"
        if pdf_to_png(str(pdf_path), str(front_png), dpi=150, page=1):
            print(f"    ✓ Generated {front_png.name}")
        else:
            print(f"    ✗ Failed to convert {front_png.name}")
            failed.append(example['name'])
        
        # For single cards, also generate back page
        if '--cards-per-page' in example['args'] and example['args'][example['args'].index('--cards-per-page') + 1] == '1':
            back_png = images_dir / f"{example['name']}-back.png"
            if pdf_to_png(str(pdf_path), str(back_png), dpi=150, page=2):
                print(f"    ✓ Generated {back_png.name}")
    
    if failed:
        print(f"\n✗ Failed to generate {len(failed)} images: {', '.join(failed)}")
        return 1
    else:
        print(f"\n✓ Successfully generated all {len(examples)} examples in docs/images/")
        return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())