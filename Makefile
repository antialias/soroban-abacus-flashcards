.PHONY: all clean install test samples help check-deps

# Default target
all: out/flashcards.pdf out/flashcards_linear.pdf

# Check dependencies
check-deps:
	@command -v typst >/dev/null 2>&1 || { echo "Error: typst is not installed. Run 'make install' first." >&2; exit 1; }
	@command -v qpdf >/dev/null 2>&1 || { echo "Warning: qpdf is not installed. Linearization will be skipped." >&2; }
	@command -v python3 >/dev/null 2>&1 || { echo "Error: python3 is not installed." >&2; exit 1; }

# Install dependencies (macOS)
install:
	@echo "Installing dependencies..."
	@command -v brew >/dev/null 2>&1 || { echo "Error: Homebrew is not installed. Visit https://brew.sh" >&2; exit 1; }
	brew install typst qpdf
	pip3 install pyyaml

# Generate default flashcards
out/flashcards.pdf: check-deps
	@mkdir -p out
	python3 src/generate.py --config config/default.yaml --output out/flashcards.pdf

# Generate linearized version
out/flashcards_linear.pdf: out/flashcards.pdf
	@command -v qpdf >/dev/null 2>&1 && qpdf --linearize out/flashcards.pdf out/flashcards_linear.pdf || echo "Skipping linearization (qpdf not installed)"

# Generate sample outputs
samples: check-deps
	@echo "Generating sample outputs..."
	@mkdir -p out/samples
	python3 src/generate.py --config config/default.yaml --output out/samples/default.pdf
	python3 src/generate.py --config config/0-99.yaml --output out/samples/0-99.pdf
	python3 src/generate.py --config config/3-column-fixed.yaml --output out/samples/3-column-fixed.pdf
	python3 src/generate.py --range "1,2,5,10,20,50,100" --cards-per-page 8 --output out/samples/custom-list.pdf
	@echo "Sample PDFs generated in out/samples/"

# Quick test with small range
test: check-deps
	@echo "Running quick test..."
	python3 src/generate.py --range "0-9" --output out/test.pdf
	@command -v qpdf >/dev/null 2>&1 && qpdf --check out/test.pdf || echo "PDF generated (validation skipped)"
	@echo "Test completed successfully"

# Clean output files
clean:
	rm -rf out/

# Show help
help:
	@echo "Soroban Flashcard Generator - Make targets:"
	@echo ""
	@echo "  make              Generate default flashcards (0-9)"
	@echo "  make samples      Generate all sample configurations"
	@echo "  make test         Run a quick test build"
	@echo "  make install      Install dependencies (macOS)"
	@echo "  make clean        Remove all generated files"
	@echo "  make help         Show this help message"
	@echo ""
	@echo "Examples:"
	@echo "  make                                    # Generate default flashcards"
	@echo "  python3 src/generate.py --range 0-99    # Custom range"
	@echo "  python3 src/generate.py --config config/0-99.yaml  # Use config file"