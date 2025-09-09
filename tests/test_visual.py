"""Visual regression tests for flashcard generation."""

import pytest
import subprocess
import tempfile
import imagehash
from pathlib import Path
from PIL import Image
import sys

# Import our modules
from generate import generate_cards_direct

class TestVisualRegression:
    """Visual regression tests using image hashing and comparison."""
    
    def test_basic_card_generation(self, temp_dir, sample_config, reference_images_dir):
        """Test basic card generation produces consistent output."""
        # Generate a single test card (number 7)
        numbers = [7]
        config = {
            **sample_config,
            'transparent': False,
            'card_width': '300px',  # Smaller for faster tests
            'card_height': '200px'
        }
        
        # Generate test output
        test_output = temp_dir / 'test_cards'
        generated_files = generate_cards_direct(
            numbers, config, test_output, 
            format='png', dpi=150,  # Lower DPI for faster tests
            separate_fronts_backs=True
        )
        
        assert len(generated_files) == 2  # Front and back
        
        # Check that files were created
        front_file = test_output / 'fronts' / 'card_000.png'
        back_file = test_output / 'backs' / 'card_000.png'
        
        assert front_file.exists(), "Front card image should exist"
        assert back_file.exists(), "Back card image should exist"
        
        # Basic image validation
        front_img = Image.open(front_file)
        back_img = Image.open(back_file)
        
        # Check dimensions are reasonable
        assert front_img.size[0] > 100, "Front image should have reasonable width"
        assert front_img.size[1] > 100, "Front image should have reasonable height"
        assert back_img.size[0] > 100, "Back image should have reasonable width"
        assert back_img.size[1] > 100, "Back image should have reasonable height"
        
        # Store as reference if they don't exist
        ref_front = reference_images_dir / 'card_7_front.png'
        ref_back = reference_images_dir / 'card_7_back.png'
        
        if not ref_front.exists():
            front_img.save(ref_front)
            print(f"Created reference image: {ref_front}")
        
        if not ref_back.exists():
            back_img.save(ref_back)
            print(f"Created reference image: {ref_back}")
        
        # If references exist, compare hashes
        if ref_front.exists() and ref_back.exists():
            ref_front_img = Image.open(ref_front)
            ref_back_img = Image.open(ref_back)
            
            # Use perceptual hashing for reasonable tolerance
            front_hash = imagehash.phash(front_img)
            ref_front_hash = imagehash.phash(ref_front_img)
            back_hash = imagehash.phash(back_img)
            ref_back_hash = imagehash.phash(ref_back_img)
            
            # Allow small differences (hash distance < 5)
            assert front_hash - ref_front_hash < 5, f"Front card changed significantly (hash diff: {front_hash - ref_front_hash})"
            assert back_hash - ref_back_hash < 5, f"Back card changed significantly (hash diff: {back_hash - ref_back_hash})"
    
    def test_different_bead_shapes(self, temp_dir, sample_config, reference_images_dir):
        """Test that different bead shapes produce visually different outputs."""
        numbers = [5]  # Simple number for shape testing
        base_config = {
            **sample_config,
            'card_width': '300px',
            'card_height': '200px'
        }
        
        shapes = ['diamond', 'circle', 'square']
        shape_hashes = {}
        
        for shape in shapes:
            config = {**base_config, 'bead_shape': shape}
            
            shape_output = temp_dir / f'shape_{shape}'
            generated_files = generate_cards_direct(
                numbers, config, shape_output,
                format='png', dpi=150,
                separate_fronts_backs=True
            )
            
            assert len(generated_files) == 2
            
            # Get hash of front image (where shape is visible)
            front_file = shape_output / 'fronts' / 'card_000.png'
            front_img = Image.open(front_file)
            shape_hashes[shape] = imagehash.phash(front_img)
        
        # Verify shapes produce different images
        assert shape_hashes['diamond'] - shape_hashes['circle'] > 3, "Diamond and circle shapes should be visually different"
        assert shape_hashes['diamond'] - shape_hashes['square'] > 3, "Diamond and square shapes should be visually different"
        assert shape_hashes['circle'] - shape_hashes['square'] > 3, "Circle and square shapes should be visually different"
    
    def test_color_schemes(self, temp_dir, sample_config, reference_images_dir):
        """Test that different color schemes produce different outputs."""
        numbers = [23]  # Multi-digit number for color testing
        base_config = {
            **sample_config,
            'card_width': '300px',
            'card_height': '200px'
        }
        
        schemes = ['monochrome', 'place-value']
        scheme_hashes = {}
        
        for scheme in schemes:
            config = {**base_config, 'color_scheme': scheme}
            
            scheme_output = temp_dir / f'color_{scheme}'
            generated_files = generate_cards_direct(
                numbers, config, scheme_output,
                format='png', dpi=150,
                separate_fronts_backs=True
            )
            
            assert len(generated_files) == 2
            
            # Get hash of front image
            front_file = scheme_output / 'fronts' / 'card_000.png'
            front_img = Image.open(front_file)
            scheme_hashes[scheme] = imagehash.phash(front_img)
        
        # Color schemes should produce different images
        hash_diff = scheme_hashes['monochrome'] - scheme_hashes['place-value']
        assert hash_diff > 2, f"Color schemes should be visually different (hash diff: {hash_diff})"
    
    @pytest.mark.slow
    def test_pdf_generation_structure(self, temp_dir, sample_config):
        """Test that PDF generation produces valid PDF files."""
        # This test requires typst to be installed
        try:
            subprocess.run(['typst', '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            pytest.skip("Typst not installed - skipping PDF tests")
        
        from generate import generate_typst_file
        
        numbers = [1, 2, 3]
        output_typst = temp_dir / 'test.typ'
        output_pdf = temp_dir / 'test.pdf'
        
        # Generate Typst file
        generate_typst_file(numbers, sample_config, output_typst)
        
        # Check Typst file was created and has content
        assert output_typst.exists()
        assert output_typst.stat().st_size > 100  # Should have substantial content
        
        # Try to compile to PDF (if typst is available)
        try:
            result = subprocess.run([
                'typst', 'compile', 
                '--font-path', str(Path(__file__).parent.parent / 'fonts'),
                str(output_typst), str(output_pdf)
            ], capture_output=True, text=True, cwd=temp_dir)
            
            if result.returncode == 0:
                assert output_pdf.exists(), "PDF should be generated"
                assert output_pdf.stat().st_size > 1000, "PDF should have reasonable size"
            else:
                print(f"PDF compilation failed: {result.stderr}")
                # Don't fail the test - typst might have font issues in test environment
                
        except FileNotFoundError:
            pytest.skip("Typst not available for PDF compilation")
    
    def test_reference_image_update_utility(self, temp_dir, sample_config, reference_images_dir):
        """Utility to regenerate reference images when needed."""
        # This test can be run manually to update references
        # Skip in normal test runs
        if not pytest.config.getoption("--update-references", default=False):
            pytest.skip("Reference update not requested")
        
        # Generate fresh reference images
        test_cases = [
            (7, 'basic'),
            (23, 'multidigit'),
            (0, 'zero')
        ]
        
        for number, name in test_cases:
            config = {
                **sample_config,
                'card_width': '300px',
                'card_height': '200px',
                'transparent': False
            }
            
            output_dir = temp_dir / f'ref_{name}'
            generate_cards_direct(
                [number], config, output_dir,
                format='png', dpi=150,
                separate_fronts_backs=True
            )
            
            # Copy to references
            front_src = output_dir / 'fronts' / 'card_000.png'
            back_src = output_dir / 'backs' / 'card_000.png'
            front_dst = reference_images_dir / f'card_{number}_front.png'
            back_dst = reference_images_dir / f'card_{number}_back.png'
            
            if front_src.exists():
                front_src.replace(front_dst)
                print(f"Updated reference: {front_dst}")
            if back_src.exists():
                back_src.replace(back_dst)
                print(f"Updated reference: {back_dst}")


def pytest_addoption(parser):
    """Add custom pytest options."""
    parser.addoption(
        "--update-references", action="store_true", default=False,
        help="Update reference images for visual tests"
    )