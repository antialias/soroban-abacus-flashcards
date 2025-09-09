"""Tests for web flashcard generation."""

import pytest
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

# Import web generator functions
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from web_generator import generate_web_flashcards, get_numeral_color, generate_card_svgs


class TestWebGeneration:
    """Test web flashcard generation functionality."""
    
    def test_get_numeral_color_monochrome(self, sample_config):
        """Test numeral color for monochrome scheme."""
        config = {**sample_config, 'color_scheme': 'monochrome', 'colored_numerals': False}
        color = get_numeral_color(42, config)
        assert color == "#333"
        
        # Even with colored numerals, monochrome should return #333
        config['colored_numerals'] = True
        color = get_numeral_color(42, config)
        assert color == "#333"
    
    def test_get_numeral_color_place_value(self, sample_config):
        """Test numeral color for place-value scheme."""
        config = {**sample_config, 'color_scheme': 'place-value', 'colored_numerals': True}
        color = get_numeral_color(42, config)
        assert color == "#222"  # Darker color for visibility
        
        # Without colored numerals, should return default
        config['colored_numerals'] = False
        color = get_numeral_color(42, config)
        assert color == "#333"
    
    @patch('generate.generate_cards_direct')
    def test_generate_card_svgs_success(self, mock_generate_cards_direct, sample_config, temp_dir):
        """Test successful SVG generation."""
        # Mock the generated files
        fronts_dir = temp_dir / 'svg_cards' / 'fronts'
        fronts_dir.mkdir(parents=True)
        
        # Create mock SVG files
        for i, num in enumerate([1, 2, 3]):
            svg_file = fronts_dir / f'card_{i:03d}.svg'
            svg_content = f'<svg width="300" height="200"><text>{num}</text></svg>'
            svg_file.write_text(svg_content)
        
        # Mock the generate_cards_direct return
        mock_generate_cards_direct.return_value = [
            fronts_dir / 'card_000.svg',
            fronts_dir / 'card_001.svg', 
            fronts_dir / 'card_002.svg',
        ]
        
        # Mock tempfile to use our temp_dir
        with patch('tempfile.TemporaryDirectory') as mock_tempdir:
            mock_tempdir.return_value.__enter__.return_value = str(temp_dir)
            
            result = generate_card_svgs([1, 2, 3], sample_config)
            
            assert len(result) == 3
            assert 1 in result
            assert 2 in result
            assert 3 in result
            assert '<svg' in result[1]
            assert '<text>1</text>' in result[1]
    
    @patch('generate.generate_cards_direct')
    def test_generate_card_svgs_fallback(self, mock_generate_cards_direct, sample_config, temp_dir):
        """Test fallback when SVG generation fails."""
        # Mock generate_cards_direct to return empty list (failure)
        mock_generate_cards_direct.return_value = []
        
        with patch('tempfile.TemporaryDirectory') as mock_tempdir:
            mock_tempdir.return_value.__enter__.return_value = str(temp_dir)
            
            result = generate_card_svgs([1, 2], sample_config)
            
            assert len(result) == 2
            assert '<svg width="300" height="200"' in result[1]
            assert 'font-size="48"' in result[1]  # Fallback SVG
    
    def test_generate_web_flashcards_structure(self, temp_dir, sample_config):
        """Test web flashcards HTML structure."""
        numbers = [7, 23]
        output_file = temp_dir / 'test.html'
        
        # Mock the SVG generation
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {
                7: '<svg width="300" height="200"><rect></rect></svg>',
                23: '<svg width="300" height="200"><circle></circle></svg>'
            }
            
            result_path = generate_web_flashcards(numbers, sample_config, output_file)
            
            assert result_path == output_file
            assert output_file.exists()
            
            content = output_file.read_text()
            
            # Check HTML structure
            assert '<!DOCTYPE html>' in content
            assert '<html lang="en">' in content
            assert '<title>Soroban Flashcards</title>' in content
            assert 'Hover over the cards to reveal the numbers' in content
            
            # Check cards are present
            assert 'data-number="7"' in content
            assert 'data-number="23"' in content
            
            # Check SVG content is embedded
            assert '<svg width="300" height="200"><rect></rect></svg>' in content
            assert '<svg width="300" height="200"><circle></circle></svg>' in content
            
            # Check CSS classes
            assert '.flashcard' in content
            assert '.numeral' in content
            assert '.abacus-container' in content
    
    def test_generate_web_flashcards_config_integration(self, temp_dir, sample_config):
        """Test that configuration options are properly integrated."""
        numbers = [42]
        output_file = temp_dir / 'test.html' 
        
        config = {
            **sample_config,
            'color_scheme': 'place-value',
            'bead_shape': 'circle',
            'colored_numerals': True,
            'font_size': '36pt',
            'font_family': 'Arial'
        }
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {42: '<svg><rect></rect></svg>'}
            
            generate_web_flashcards(numbers, config, output_file)
            content = output_file.read_text()
            
            # Check config values are used
            assert 'font-family: Arial' in content
            assert '36pt' in content
            assert 'place value' in content.lower()
            assert 'Circle' in content  # Bead shape capitalized
    
    def test_generate_web_flashcards_empty_numbers(self, temp_dir, sample_config):
        """Test handling of empty numbers list."""
        output_file = temp_dir / 'empty.html'
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {}
            
            result_path = generate_web_flashcards([], sample_config, output_file)
            
            assert result_path == output_file
            assert output_file.exists()
            
            content = output_file.read_text()
            assert '<title>Soroban Flashcards</title>' in content
            assert 'Cards:</strong> 0' in content
            assert 'Range:</strong> 0' in content
    
    def test_web_flashcards_responsive_design(self, temp_dir, sample_config):
        """Test that responsive CSS is included."""
        numbers = [1]
        output_file = temp_dir / 'responsive.html'
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {1: '<svg><rect></rect></svg>'}
            
            generate_web_flashcards(numbers, sample_config, output_file)
            content = output_file.read_text()
            
            # Check mobile responsiveness
            assert '@media (max-width: 768px)' in content
            assert 'grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))' in content
            
            # Check print styles
            assert '@media print' in content
            assert 'break-inside: avoid' in content
    
    def test_web_flashcards_accessibility(self, temp_dir, sample_config):
        """Test accessibility features."""
        numbers = [5]
        output_file = temp_dir / 'accessible.html'
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {5: '<svg><rect></rect></svg>'}
            
            generate_web_flashcards(numbers, sample_config, output_file)
            content = output_file.read_text()
            
            # Check accessibility attributes
            assert 'lang="en"' in content
            assert 'charset="UTF-8"' in content
            assert 'viewport' in content
            
            # Check that hover states don't rely only on hover
            assert 'cursor: pointer' in content
            assert 'transition:' in content