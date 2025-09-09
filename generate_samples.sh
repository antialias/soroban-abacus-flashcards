#!/bin/bash

# Generate sample PDFs for demonstration
# This script creates sample outputs once Typst is installed

set -e

echo "Checking dependencies..."
if ! command -v typst &> /dev/null; then
    echo "Error: Typst is not installed. Please run 'make install' first."
    exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed."
    exit 1
fi

echo "Creating output directories..."
mkdir -p out/samples

echo "Generating sample PDFs..."

# 1. Default 0-9 set
echo "  1/5: Default (0-9)..."
python3 src/generate.py \
    --config config/default.yaml \
    --output out/samples/default_0-9.pdf

# 2. 0-99 with cut marks
echo "  2/5: 0-99 with cut marks..."
python3 src/generate.py \
    --config config/0-99.yaml \
    --output out/samples/0-99_with_cuts.pdf

# 3. 3-column fixed width (0-999)
echo "  3/5: 3-column fixed (0-999)..."
python3 src/generate.py \
    --config config/3-column-fixed.yaml \
    --range "0-20" \
    --output out/samples/3-column_sample.pdf

# 4. Custom list with 8 cards per page
echo "  4/5: Custom list (8 per page)..."
python3 src/generate.py \
    --range "1,2,5,10,20,50,100,500" \
    --cards-per-page 8 \
    --font-size "36pt" \
    --output out/samples/custom_list_8up.pdf

# 5. Shuffled deck with seed
echo "  5/5: Shuffled 0-20..."
python3 src/generate.py \
    --range "0-20" \
    --shuffle \
    --seed 42 \
    --show-empty-columns \
    --columns 2 \
    --output out/samples/shuffled_0-20.pdf

echo ""
echo "Sample generation complete!"
echo "Generated files:"
ls -lh out/samples/*.pdf 2>/dev/null || echo "  (PDFs will appear here once generated)"
echo ""
echo "Note: If Typst is not installed, run:"
echo "  brew install typst"
echo "  ./generate_samples.sh"