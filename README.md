# Soroban Flashcard Generator

A vector-based PDF flashcard generator for learning soroban (Japanese abacus) numbers. Creates double-sided flashcards with soroban bead representations on the front and Arabic numerals on the back.

## Features

- **Pure vector graphics** - All soroban diagrams and text are rendered as vectors
- **Configurable layouts** - Default 6 cards per US Letter page, customizable
- **Duplex printing ready** - Automatic front/back alignment for double-sided printing
- **Embedded fonts** - Bundled DejaVu Sans for consistent output
- **Flexible number ranges** - Generate cards for any range or custom list
- **macOS optimized** - Minimal dependencies, works great on Mac

## Quick Start

### Prerequisites

- macOS (tested on latest versions)
- Python 3 (included with macOS)
- Typst (PDF generation engine)
- qpdf (optional, for linearization)

### Installation

```bash
# Install dependencies
make install

# Or manually:
brew install typst qpdf
pip3 install pyyaml
```

### Generate Flashcards

```bash
# Generate default set (0-9)
make

# Generate from config file
python3 src/generate.py --config config/0-99.yaml

# Custom range
python3 src/generate.py --range 0-99

# Custom list of numbers
python3 src/generate.py --range "1,2,5,10,20,50,100"

# With shuffle
python3 src/generate.py --range 0-99 --shuffle --seed 42
```

## Configuration

### Using Configuration Files

Create a YAML or JSON file with your preferences:

```yaml
range: "0-99"
cards_per_page: 6
paper_size: "us-letter"
orientation: "portrait"
margins:
  top: "0.5in"
  bottom: "0.5in"
  left: "0.5in"
  right: "0.5in"
gutter: "5mm"
show_cut_marks: true
show_registration: true
font_family: "DejaVu Sans"
font_size: "48pt"
columns: auto
show_empty_columns: false
shuffle: false
seed: 42  # For deterministic shuffling
```

### Command-Line Options

```bash
python3 src/generate.py [OPTIONS]

Options:
  --config, -c FILE           Configuration file (JSON or YAML)
  --range, -r RANGE          Number range (e.g., "0-99") or list (e.g., "1,2,5")
  --cards-per-page N         Cards per page (default: 6, options: 4,6,8,9)
  --paper-size SIZE          Paper size (default: us-letter)
  --orientation ORIENT       Page orientation (portrait/landscape)
  --margins T,R,B,L          Margins (e.g., "0.5in,0.5in,0.5in,0.5in")
  --gutter SIZE              Space between cards (default: 5mm)
  --shuffle                  Shuffle the numbers
  --seed N                   Random seed for deterministic shuffle
  --cut-marks                Show cut marks
  --registration             Show registration marks for alignment
  --font-family FONT         Font family (default: DejaVu Sans)
  --font-size SIZE           Font size (default: 48pt)
  --columns N                Soroban columns (auto or number)
  --show-empty-columns       Show leading empty columns
  --output, -o FILE          Output PDF path (default: out/flashcards.pdf)
  --linearize                Create linearized PDF (default: true)
```

## Soroban Representation

The soroban is rendered with:
- **1 heaven bead** (worth 5) per column
- **4 earth beads** (worth 1 each) per column
- **Active beads** shown in black, moved toward the reckoning bar
- **Inactive beads** shown in light gray, away from the bar
- **Columns** represent place values (ones, tens, hundreds, etc.)

### Column Display Options

- `columns: auto` - Shows minimal columns needed
- `columns: 3` - Always shows 3 columns (e.g., for 0-999)
- `show_empty_columns: true` - Shows leading zeros
- `show_empty_columns: false` - Suppresses leading zeros

## Print Settings

### For Best Results

1. **Paper**: US Letter (8.5" × 11") or A4
2. **Margins**: Default 0.5" works with most printers
3. **Duplex**: Long-edge binding, automatic duplex
4. **Cut marks**: Enable with `--cut-marks` for easier cutting
5. **Registration**: Enable with `--registration` for alignment verification

### Sample Configurations

- `config/default.yaml` - Basic 0-9 set
- `config/0-99.yaml` - Two-digit numbers with cut marks
- `config/3-column-fixed.yaml` - Three-digit numbers, fixed width

## Project Structure

```
soroban-abacus-flashcards/
├── src/
│   └── generate.py         # Main CLI tool
├── templates/
│   └── flashcards.typ      # Typst template with soroban rendering
├── config/
│   ├── default.yaml        # Default configuration
│   ├── 0-99.yaml          # 0-99 range config
│   └── 3-column-fixed.yaml # 3-column fixed width config
├── fonts/
│   ├── DejaVuSans.ttf     # Bundled font
│   └── DejaVuSans-Bold.ttf # Bold variant
├── out/                    # Generated PDFs (created on first run)
├── Makefile               # Build automation
└── README.md              # This file
```

## Design Notes

### Soroban Number Mapping

Numbers are decomposed into heaven (5s) and earth (1s) beads:
- **7** = 1 heaven bead (5) + 2 earth beads (2×1)
- **23** = Tens: 4 earth beads (4×1), Ones: 3 earth beads (3×1)
- **156** = Hundreds: 1 heaven + 0 earth, Tens: 1 heaven + 0 earth, Ones: 1 heaven + 1 earth

### Duplex Alignment

- Front cards are laid out left-to-right, top-to-bottom
- Back cards are mirrored horizontally for long-edge binding
- Registration marks (optional) help verify alignment
- Safe margins ensure content isn't lost when cutting

### Vector Graphics

All elements are rendered as vectors using Typst's drawing primitives:
- Beads are vector circles with stroke
- Rods and reckoning bar are vector rectangles
- No rasterization ensures crisp output at any scale

## Troubleshooting

### "typst command not found"
Run `make install` or `brew install typst`

### "qpdf command not found"
PDF will generate but won't be linearized. Install with `brew install qpdf`

### Fonts not embedding
Ensure the `fonts/` directory contains the DejaVu TTF files

### Misaligned duplex printing
- Check printer duplex settings (should be long-edge)
- Enable registration marks with `--registration`
- Verify margins match your printer's capabilities

## Examples

```bash
# Generate samples
make samples

# Quick test
make test

# Clean all outputs
make clean

# Show help
make help
```

## License

This project uses DejaVu Sans font (included), which is released under a free license. The generator code is provided as-is for educational use.