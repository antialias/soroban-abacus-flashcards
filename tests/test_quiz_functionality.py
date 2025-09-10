"""Tests for quiz functionality in web flashcards."""

import pytest
import tempfile
from pathlib import Path
from unittest.mock import patch

# Import web generator functions
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from web_generator import generate_web_flashcards


class TestQuizFunctionality:
    """Test quiz functionality in web flashcards."""
    
    def test_quiz_html_structure(self, temp_dir, sample_config):
        """Test that quiz HTML structure is present."""
        numbers = [1, 2, 3, 4, 5]
        output_file = temp_dir / 'quiz_test.html'
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {i: f'<svg><text>{i}</text></svg>' for i in numbers}
            
            generate_web_flashcards(numbers, sample_config, output_file)
            content = output_file.read_text()
            
            # Check quiz section is present
            assert 'quiz-section' in content
            assert 'quiz-controls' in content
            
            # Check quiz control elements  
            assert 'data-count="5"' in content
            assert 'data-count="10"' in content
            assert 'data-count="15"' in content
            assert 'data-count="25"' in content
            assert 'data-count="all"' in content
            assert 'id="display-time"' in content
            assert 'id="start-quiz"' in content
            
            # Check quiz display elements
            assert 'quiz-game' in content
            assert 'quiz-input' in content
            assert 'quiz-results' in content
    
    def test_quiz_javascript_classes(self, temp_dir, sample_config):
        """Test that quiz JavaScript classes and methods are defined."""
        numbers = [7, 14, 21]
        output_file = temp_dir / 'quiz_js_test.html'
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {i: f'<svg><text>{i}</text></svg>' for i in numbers}
            
            generate_web_flashcards(numbers, sample_config, output_file)
            content = output_file.read_text()
            
            # Check SorobanQuiz class is defined
            assert 'class SorobanQuiz' in content
            assert 'constructor()' in content
            assert 'initializeCards()' in content
            assert 'bindEvents()' in content
            assert 'startQuiz()' in content
            assert 'showNextCard()' in content
            assert 'showCountdown()' in content
            assert 'displayCard(' in content
            assert 'showInputPhase()' in content
            assert 'submitAnswers()' in content
            assert 'calculateScore()' in content
            assert 'showResults()' in content
            assert 'resetQuiz()' in content
    
    def test_quiz_default_values(self, temp_dir, sample_config):
        """Test quiz default configuration values."""
        numbers = list(range(1, 26))  # 25 cards
        output_file = temp_dir / 'quiz_defaults_test.html'
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {i: f'<svg><text>{i}</text></svg>' for i in numbers}
            
            generate_web_flashcards(numbers, sample_config, output_file)
            content = output_file.read_text()
            
            # Check default timing (2 seconds)
            assert 'value="2"' in content and 'id="display-time"' in content
            assert 'min="0.5"' in content and 'max="10"' in content
            assert 'step="0.5"' in content
            
            # Check default card count initialization
            assert 'this.selectedCount = 15' in content
            assert 'this.displayTime = 2.0' in content
            
            # Check that 15 cards button is initially selected
            assert 'active" data-count="15"' in content
    
    def test_quiz_card_count_buttons(self, temp_dir, sample_config):
        """Test card count button logic."""
        numbers = list(range(1, 101))  # 100 cards
        output_file = temp_dir / 'quiz_buttons_test.html'
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {i: f'<svg><text>{i}</text></svg>' for i in numbers}
            
            generate_web_flashcards(numbers, sample_config, output_file)
            content = output_file.read_text()
            
            # Check all button values are present
            assert '>5</button>' in content
            assert '>10</button>' in content  
            assert '>15</button>' in content
            assert '>25</button>' in content
            assert '>All (100)</button>' in content
            
            # Check button data attributes
            assert 'data-count="5"' in content
            assert 'data-count="10"' in content
            assert 'data-count="15"' in content
            assert 'data-count="25"' in content
            assert 'data-count="all"' in content
    
    def test_quiz_progress_tracking(self, temp_dir, sample_config):
        """Test quiz progress tracking elements."""
        numbers = [3, 6, 9]
        output_file = temp_dir / 'quiz_progress_test.html'
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {i: f'<svg><text>{i}</text></svg>' for i in numbers}
            
            generate_web_flashcards(numbers, sample_config, output_file)
            content = output_file.read_text()
            
            # Check progress elements
            assert 'progress-bar' in content
            assert 'progress-fill' in content
            assert 'progress-text' in content
            assert 'id="current-card"' in content
            assert 'id="total-cards"' in content
            
            # Check progress update logic
            assert 'progress-fill' in content
            assert 'style.width' in content
    
    def test_quiz_input_validation(self, temp_dir, sample_config):
        """Test quiz answer input validation."""
        numbers = [42, 108, 999]
        output_file = temp_dir / 'quiz_input_test.html'
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {i: f'<svg><text>{i}</text></svg>' for i in numbers}
            
            generate_web_flashcards(numbers, sample_config, output_file)
            content = output_file.read_text()
            
            # Check answer input elements
            assert 'quiz-input' in content
            assert 'placeholder="e.g., 23, 45, 67 or 23 45 67"' in content
            
            # Check input parsing logic
            assert 'parseAnswers(' in content
            assert 'split(' in content
            assert '.trim()' in content
            assert '.filter(' in content
            assert 'parseInt(' in content
    
    def test_quiz_scoring_logic(self, temp_dir, sample_config):
        """Test quiz scoring calculation."""
        numbers = [5, 10, 15, 20]
        output_file = temp_dir / 'quiz_scoring_test.html'
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {i: f'<svg><text>{i}</text></svg>' for i in numbers}
            
            generate_web_flashcards(numbers, sample_config, output_file)
            content = output_file.read_text()
            
            # Check scoring elements
            assert 'calculateScore()' in content
            assert 'showResults()' in content
            assert 'quiz-results' in content
            
            # Check score calculation logic
            assert 'correctAnswers' in content
            assert 'percentage' in content
            assert 'Math.round(' in content
            
            # Check results display elements
            assert 'score-display' in content
    
    def test_quiz_countdown_functionality(self, temp_dir, sample_config):
        """Test quiz countdown display."""
        numbers = [1, 2]
        output_file = temp_dir / 'quiz_countdown_test.html'
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {i: f'<svg><text>{i}</text></svg>' for i in numbers}
            
            generate_web_flashcards(numbers, sample_config, output_file)
            content = output_file.read_text()
            
            # Check countdown elements
            assert 'countdown' in content
            assert 'showCountdown()' in content
            
            # Check countdown animation
            assert 'setTimeout(' in content
    
    def test_quiz_responsive_design(self, temp_dir, sample_config):
        """Test quiz responsive CSS."""
        numbers = [8]
        output_file = temp_dir / 'quiz_responsive_test.html'
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {i: f'<svg><text>{i}</text></svg>' for i in numbers}
            
            generate_web_flashcards(numbers, sample_config, output_file)
            content = output_file.read_text()
            
            # Check responsive CSS classes
            assert '.quiz-section' in content
            assert '.quiz-controls' in content
            assert '.count-buttons' in content
            
            # Check mobile responsiveness
            assert '@media (max-width: 768px)' in content
    
    def test_quiz_accessibility(self, temp_dir, sample_config):
        """Test quiz accessibility features."""
        numbers = [11]
        output_file = temp_dir / 'quiz_accessibility_test.html'
        
        with patch('web_generator.generate_card_svgs') as mock_svg_gen:
            mock_svg_gen.return_value = {i: f'<svg><text>{i}</text></svg>' for i in numbers}
            
            generate_web_flashcards(numbers, sample_config, output_file)
            content = output_file.read_text()
            
            # Check semantic HTML
            assert '<button' in content
            assert '<label' in content
            assert 'for=' in content
    
    def test_quiz_with_different_card_counts(self, temp_dir, sample_config):
        """Test quiz functionality with different total card counts."""
        test_cases = [
            ([1], "All (1)"),  # Single card
            (list(range(1, 4)), "All (3)"),  # Few cards  
            (list(range(1, 16)), "All (15)"),  # Exactly 15 cards
            (list(range(1, 51)), "All (50)"),  # Many cards
        ]
        
        for numbers, expected_all_text in test_cases:
            output_file = temp_dir / f'quiz_count_{len(numbers)}_test.html'
            
            with patch('web_generator.generate_card_svgs') as mock_svg_gen:
                mock_svg_gen.return_value = {i: f'<svg><text>{i}</text></svg>' for i in numbers}
                
                generate_web_flashcards(numbers, sample_config, output_file)
                content = output_file.read_text()
                
                # Check that "All" button shows correct count
                assert expected_all_text in content
                
                # Check that card selection buttons are present
                assert 'data-count="all"' in content