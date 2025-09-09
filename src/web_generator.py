#!/usr/bin/env python3
"""
Web flashcard generator for Soroban abacus cards.
Generates static HTML with inline SVG abacus representations using existing Typst->SVG pipeline.
"""

import tempfile
from pathlib import Path


def get_numeral_color(number, config):
    """Get color for numeral based on configuration.""" 
    if not config.get('colored_numerals', False):
        return "#333"
        
    color_scheme = config.get('color_scheme', 'monochrome')
    if color_scheme == 'monochrome':
        return "#333"
    else:
        # For colored schemes, use a darker color for visibility
        return "#222"


def generate_card_svgs(numbers, config):
    """Generate SVG content for each flashcard using existing Typst pipeline."""
    from generate import generate_cards_direct
    
    # Create temporary directory for SVG generation
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        svg_dir = tmpdir_path / 'svg_cards'
        
        # Configure for web-optimized SVGs
        web_config = {
            **config,
            'card_width': '4in',  # Fixed size for web (Typst needs units)
            'card_height': '2.5in',
            'transparent': True,  # Transparent background for web
            'scale_factor': 0.8   # Slightly smaller for web
        }
        
        # Generate SVG files using existing pipeline
        generated_files = generate_cards_direct(
            numbers, web_config, svg_dir,
            format='svg', separate_fronts_backs=True
        )
        
        # Read SVG contents
        card_data = {}
        fronts_dir = svg_dir / 'fronts'
        
        for i, number in enumerate(numbers):
            front_file = fronts_dir / f'card_{i:03d}.svg'
            if front_file.exists():
                with open(front_file, 'r') as f:
                    svg_content = f.read()
                    # Remove XML declaration and DOCTYPE if present
                    if svg_content.startswith('<?xml'):
                        svg_content = svg_content.split('>', 1)[1]
                    card_data[number] = svg_content.strip()
            else:
                # Fallback if SVG generation failed
                card_data[number] = f'<svg width="300" height="200"><text x="150" y="100" text-anchor="middle" font-size="48">{number}</text></svg>'
        
        return card_data


def generate_web_flashcards(numbers, config, output_path):
    """Generate HTML file with flashcard layout."""
    
    # Generate SVG content for all cards
    print(f"Generating SVG content for {len(numbers)} cards...")
    card_svgs = generate_card_svgs(numbers, config)
    
    # Generate individual cards HTML
    cards_html = []
    for i, number in enumerate(numbers):
        svg_content = card_svgs.get(number, f'<svg width="300" height="200"><text x="150" y="100" text-anchor="middle" font-size="48">Error</text></svg>')
        numeral_color = get_numeral_color(number, config)
        
        card_html = f'''
        <div class="flashcard" data-number="{number}">
            <div class="card-number">#{i+1}</div>
            <div class="abacus-container">
                {svg_content}
            </div>
            <div class="numeral" style="color: {numeral_color};">{number}</div>
        </div>'''
        
        cards_html.append(card_html)
    
    # Configuration descriptions
    color_schemes = {
        'monochrome': 'All beads are the same color',
        'place-value': 'Each place value (ones, tens, hundreds) has a different color',
        'heaven-earth': 'Heaven beads (5-value) and earth beads (1-value) have different colors',
        'alternating': 'Columns alternate between two colors'
    }
    
    color_scheme_description = color_schemes.get(
        config.get('color_scheme', 'monochrome'),
        'Monochrome color scheme'
    )
    
    # Format font size for CSS
    font_size = config.get('font_size', '48pt')
    if not font_size.endswith(('px', 'pt', 'em', 'rem', '%')):
        font_size = font_size + 'px'  # Add px if no unit specified
    
    # HTML template
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soroban Flashcards</title>
    <style>
        body {{
            font-family: {font_family}, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        
        .header h1 {{
            color: #333;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            color: #666;
            font-size: 1.2em;
        }}
        
        .cards-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        
        .flashcard {{
            background: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            cursor: pointer;
            position: relative;
            min-height: 220px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}
        
        .flashcard:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        }}
        
        .abacus-container {{
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 10px 0;
            max-width: 100%;
            overflow: hidden;
        }}
        
        .abacus-container svg {{
            max-width: 100%;
            height: auto;
        }}
        
        .numeral {{
            font-size: {font_size};
            font-weight: bold;
            color: {numeral_color};
            opacity: 0;
            transition: opacity 0.3s ease;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(255,255,255,0.95);
            padding: 15px 25px;
            border-radius: 8px;
            border: 2px solid #ddd;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            z-index: 10;
        }}
        
        .flashcard:hover .numeral {{
            opacity: 1;
        }}
        
        .card-number {{
            position: absolute;
            top: 10px;
            left: 10px;
            font-size: 0.8em;
            color: #999;
            background: rgba(255,255,255,0.8);
            padding: 2px 6px;
            border-radius: 4px;
        }}
        
        .instructions {{
            text-align: center;
            margin: 30px 0;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .instructions h3 {{
            color: #333;
            margin-bottom: 10px;
        }}
        
        .instructions p {{
            color: #666;
            line-height: 1.5;
        }}
        
        .stats {{
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
        }}
        
        .stats div {{
            background: #f8f9fa;
            padding: 10px 15px;
            border-radius: 6px;
            font-size: 0.9em;
        }}
        
        @media (max-width: 768px) {{
            .cards-grid {{
                grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
                gap: 15px;
            }}
            
            .flashcard {{
                min-height: 200px;
                padding: 15px;
            }}
            
            .numeral {{
                font-size: calc({font_size} * 0.8);
                padding: 10px 20px;
            }}
        }}
        
        @media print {{
            body {{
                background-color: white;
            }}
            .flashcard {{
                box-shadow: none;
                border: 1px solid #ddd;
                break-inside: avoid;
            }}
            .numeral {{
                opacity: 0.5;
                background: transparent;
                border: none;
                box-shadow: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Soroban Flashcards</h1>
            <p>Hover over the cards to reveal the numbers</p>
        </div>
        
        <div class="instructions">
            <h3>How to use these flashcards:</h3>
            <p>Look at each abacus representation and try to determine the number before hovering to reveal the answer. 
            The abacus shows numbers using beads: each column represents a place value (ones, tens, hundreds, etc.). 
            In each column, the top bead represents 5 and the bottom beads each represent 1.</p>
            
            <div class="stats">
                <div><strong>Cards:</strong> {card_count}</div>
                <div><strong>Range:</strong> {number_range}</div>
                <div><strong>Color Scheme:</strong> {color_scheme_description}</div>
                <div><strong>Bead Shape:</strong> {bead_shape}</div>
            </div>
        </div>
        
        <div class="cards-grid">
            {cards_html}
        </div>
        
        <div class="instructions">
            <p><em>Tip: You can print these cards for offline practice. Numbers will be faintly visible in print mode.</em></p>
        </div>
    </div>
</body>
</html>'''
    
    # Fill template
    html_content = html_template.format(
        font_family=config.get('font_family', 'DejaVu Sans').replace('"', ''),
        font_size=font_size,
        numeral_color=get_numeral_color(numbers[0] if numbers else 0, config),
        cards_html=''.join(cards_html),
        color_scheme_description=color_scheme_description,
        bead_shape=config.get('bead_shape', 'diamond').capitalize(),
        card_count=len(numbers),
        number_range=f"{min(numbers)} - {max(numbers)}" if numbers else "0"
    )
    
    # Write HTML file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Generated web flashcards: {output_path}")
    return output_path