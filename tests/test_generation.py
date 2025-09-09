"""Tests for core generation functionality."""

import pytest
import tempfile
from pathlib import Path

from generate import generate_single_card_typst, generate_typst_file


class TestTypstGeneration:
    """Test Typst file generation functions."""
    
    def test_generate_single_card_typst_front(self, temp_dir, sample_config):
        """Test generation of single card Typst file for front side."""
        output_file = temp_dir / 'card_front.typ'
        
        generate_single_card_typst(
            number=7,
            side='front',
            config=sample_config,
            output_path=output_file,
            project_root=temp_dir
        )
        
        assert output_file.exists()
        
        content = output_file.read_text()
        assert '#import "single-card.typ"' in content
        assert 'generate-single-card' in content
        assert '7,' in content  # Number should be in the content
        assert 'side: "front"' in content
        assert 'bead-shape: "diamond"' in content  # From sample config
    
    def test_generate_single_card_typst_back(self, temp_dir, sample_config):
        """Test generation of single card Typst file for back side."""
        output_file = temp_dir / 'card_back.typ'
        
        generate_single_card_typst(
            number=42,
            side='back',
            config=sample_config,
            output_path=output_file,
            project_root=temp_dir
        )
        
        assert output_file.exists()
        
        content = output_file.read_text()
        assert 'side: "back"' in content
        assert '42,' in content
    
    def test_generate_single_card_with_custom_config(self, temp_dir):
        """Test single card generation with custom configuration."""
        custom_config = {
            'bead_shape': 'circle',
            'color_scheme': 'place-value',
            'colored_numerals': True,
            'hide_inactive_beads': True,
            'transparent': True,
            'card_width': '4in',
            'card_height': '3in',
            'font_size': '36pt',
            'font_family': 'Arial',
            'scale_factor': 1.2
        }
        
        output_file = temp_dir / 'custom_card.typ'
        
        generate_single_card_typst(
            number=123,
            side='front',
            config=custom_config,
            output_path=output_file,
            project_root=temp_dir
        )
        
        content = output_file.read_text()
        assert 'bead-shape: "circle"' in content
        assert 'color-scheme: "place-value"' in content
        assert 'colored-numerals: true' in content
        assert 'hide-inactive-beads: true' in content
        assert 'transparent: true' in content
        assert 'width: 4in' in content
        assert 'height: 3in' in content
        assert 'font-size: 36pt' in content
        assert 'font-family: "Arial"' in content
        assert 'scale-factor: 1.2' in content
    
    def test_generate_typst_file_basic(self, temp_dir, sample_config):
        """Test generation of multi-card Typst file."""
        numbers = [1, 2, 3, 5, 8]
        output_file = temp_dir / 'flashcards.typ'
        
        generate_typst_file(numbers, sample_config, output_file)
        
        assert output_file.exists()
        
        content = output_file.read_text()
        assert '#import "templates/flashcards.typ"' in content
        assert 'generate-flashcards' in content
        assert '(1, 2, 3, 5, 8,)' in content  # Numbers array
        assert 'cards-per-page: 6' in content  # From sample config
    
    def test_generate_typst_file_with_margins(self, temp_dir):
        """Test Typst generation with custom margins."""
        config = {
            'cards_per_page': 4,
            'paper_size': 'a4',
            'orientation': 'landscape',
            'margins': {
                'top': '1in',
                'bottom': '0.75in',
                'left': '0.5in',
                'right': '0.5in'
            },
            'gutter': '10mm',
            'font_family': 'Times',
            'font_size': '36pt'
        }
        
        numbers = [10, 20, 30]
        output_file = temp_dir / 'custom_flashcards.typ'
        
        generate_typst_file(numbers, config, output_file)
        
        content = output_file.read_text()
        assert 'paper-size: "a4"' in content
        assert 'orientation: "landscape"' in content
        assert 'top: 1in' in content
        assert 'bottom: 0.75in' in content
        assert 'gutter: 10mm' in content
        assert 'font-family: "Times"' in content
    
    def test_generate_typst_file_boolean_options(self, temp_dir):
        """Test Typst generation with boolean configuration options."""
        config = {
            'cards_per_page': 6,
            'show_cut_marks': True,
            'show_registration': False,
            'show_empty_columns': True,
            'hide_inactive_beads': False,
            'colored_numerals': True
        }
        
        numbers = [7]
        output_file = temp_dir / 'boolean_test.typ'
        
        generate_typst_file(numbers, config, output_file)
        
        content = output_file.read_text()
        assert 'show-cut-marks: true' in content
        assert 'show-registration: false' in content
        assert 'show-empty-columns: true' in content
        assert 'hide-inactive-beads: false' in content
        assert 'colored-numerals: true' in content
    
    def test_generate_typst_file_empty_numbers(self, temp_dir, sample_config):
        """Test handling of empty numbers list."""
        numbers = []
        output_file = temp_dir / 'empty.typ'
        
        generate_typst_file(numbers, sample_config, output_file)
        
        content = output_file.read_text()
        assert '()' in content  # Empty array
    
    def test_generate_typst_file_single_number(self, temp_dir, sample_config):
        """Test generation with single number."""
        numbers = [99]
        output_file = temp_dir / 'single.typ'
        
        generate_typst_file(numbers, sample_config, output_file)
        
        content = output_file.read_text()
        assert '(99,)' in content  # Single element array with trailing comma


class TestConfigDefaults:
    """Test default value handling in generation functions."""
    
    def test_single_card_defaults(self, temp_dir):
        """Test that single card generation handles missing config gracefully."""
        minimal_config = {}
        output_file = temp_dir / 'defaults.typ'
        
        generate_single_card_typst(
            number=5,
            side='front',
            config=minimal_config,
            output_path=output_file,
            project_root=temp_dir
        )
        
        content = output_file.read_text()
        # Should use defaults from the function
        assert 'bead-shape: "diamond"' in content
        assert 'color-scheme: "monochrome"' in content
        assert 'colored-numerals: false' in content
        assert 'hide-inactive-beads: false' in content
        assert 'columns: auto' in content
        assert 'font-family: "DejaVu Sans"' in content
    
    def test_typst_file_defaults(self, temp_dir):
        """Test that multi-card generation handles missing config gracefully."""
        minimal_config = {}
        numbers = [1, 2]
        output_file = temp_dir / 'defaults.typ'
        
        generate_typst_file(numbers, minimal_config, output_file)
        
        content = output_file.read_text()
        # Should use defaults
        assert 'cards-per-page: 6' in content
        assert 'paper-size: "us-letter"' in content
        assert 'orientation: "portrait"' in content
        assert 'font-family: "DejaVu Sans"' in content


class TestEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_large_numbers(self, temp_dir, sample_config):
        """Test generation with large numbers."""
        large_numbers = [999, 1000, 9999]
        output_file = temp_dir / 'large.typ'
        
        generate_typst_file(large_numbers, sample_config, output_file)
        
        content = output_file.read_text()
        assert '(999, 1000, 9999,)' in content
    
    def test_zero_handling(self, temp_dir, sample_config):
        """Test generation with zero."""
        numbers = [0]
        output_file = temp_dir / 'zero.typ'
        
        generate_single_card_typst(
            number=0,
            side='front',
            config=sample_config,
            output_path=output_file,
            project_root=temp_dir
        )
        
        content = output_file.read_text()
        assert '0,' in content  # Zero should be handled correctly
    
    def test_special_characters_in_paths(self, temp_dir, sample_config):
        """Test generation with paths containing spaces."""
        numbers = [5]
        # Create directory with spaces
        special_dir = temp_dir / 'path with spaces'
        special_dir.mkdir()
        output_file = special_dir / 'test file.typ'
        
        generate_typst_file(numbers, sample_config, output_file)
        
        assert output_file.exists()
        content = output_file.read_text()
        assert '(5,)' in content