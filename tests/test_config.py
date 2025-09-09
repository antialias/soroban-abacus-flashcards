"""Tests for configuration loading and parsing."""

import pytest
import json
import yaml
import tempfile
from pathlib import Path

from generate import load_config, parse_range


class TestConfigLoading:
    """Test configuration file loading."""
    
    def test_load_yaml_config(self, temp_dir):
        """Test loading YAML configuration files."""
        config_data = {
            'range': '0-9',
            'cards_per_page': 4,
            'bead_shape': 'circle'
        }
        
        config_file = temp_dir / 'test.yaml'
        with open(config_file, 'w') as f:
            yaml.dump(config_data, f)
        
        loaded = load_config(str(config_file))
        assert loaded == config_data
    
    def test_load_json_config(self, temp_dir):
        """Test loading JSON configuration files."""
        config_data = {
            'range': '0-99',
            'color_scheme': 'place-value',
            'margins': {'top': '1in', 'bottom': '1in'}
        }
        
        config_file = temp_dir / 'test.json'
        with open(config_file, 'w') as f:
            json.dump(config_data, f)
        
        loaded = load_config(str(config_file))
        assert loaded == config_data
    
    def test_load_nonexistent_config(self):
        """Test handling of nonexistent config files."""
        with pytest.raises(FileNotFoundError):
            load_config('nonexistent.yaml')


class TestRangeParsing:
    """Test number range parsing functionality."""
    
    def test_parse_simple_range(self):
        """Test parsing simple ranges like '0-9'."""
        result = parse_range('0-9')
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert result == expected
    
    def test_parse_range_with_step(self):
        """Test parsing ranges with custom steps."""
        result = parse_range('0-10', step=2)
        expected = [0, 2, 4, 6, 8, 10]
        assert result == expected
        
        result = parse_range('0-20', step=5)
        expected = [0, 5, 10, 15, 20]
        assert result == expected
    
    def test_parse_comma_list(self):
        """Test parsing comma-separated number lists."""
        result = parse_range('1,5,10,25')
        expected = [1, 5, 10, 25]
        assert result == expected
    
    def test_parse_mixed_list_and_ranges(self):
        """Test parsing mixed comma-separated values with ranges."""
        result = parse_range('1,5-7,10')
        expected = [1, 5, 6, 7, 10]
        assert result == expected
    
    def test_parse_single_number(self):
        """Test parsing single numbers."""
        result = parse_range('42')
        expected = [42]
        assert result == expected
    
    def test_parse_negative_numbers(self):
        """Test handling of negative numbers (edge case)."""
        # Note: The current implementation might not handle this correctly
        # This test documents the expected behavior
        with pytest.raises(ValueError):
            parse_range('-5-5')
    
    def test_parse_invalid_range(self):
        """Test handling of invalid range strings."""
        with pytest.raises(ValueError):
            parse_range('invalid')
        
        with pytest.raises(ValueError):
            parse_range('10-5')  # End before start
    
    def test_parse_large_range(self):
        """Test parsing large ranges."""
        result = parse_range('0-100', step=25)
        expected = [0, 25, 50, 75, 100]
        assert result == expected
    
    def test_parse_step_ignored_for_lists(self):
        """Test that step parameter is ignored for comma-separated lists."""
        result = parse_range('1,2,3,4', step=10)  # Step should be ignored
        expected = [1, 2, 3, 4]
        assert result == expected


class TestConfigIntegration:
    """Integration tests for configuration handling."""
    
    def test_real_config_files(self, project_root):
        """Test loading real configuration files from the project."""
        config_dir = project_root / 'config'
        
        # Test default config
        default_config = config_dir / 'default.yaml'
        if default_config.exists():
            config = load_config(str(default_config))
            assert 'range' in config
            assert 'cards_per_page' in config
    
    def test_config_with_range_parsing(self, temp_dir):
        """Test integration of config loading with range parsing."""
        config_data = {
            'range': '5-15',
            'step': 2,
            'cards_per_page': 8
        }
        
        config_file = temp_dir / 'test.yaml'
        with open(config_file, 'w') as f:
            yaml.dump(config_data, f)
        
        config = load_config(str(config_file))
        numbers = parse_range(config['range'], config.get('step', 1))
        
        expected = [5, 7, 9, 11, 13, 15]
        assert numbers == expected
    
    def test_config_defaults(self, sample_config):
        """Test that sample config has reasonable defaults."""
        assert sample_config['cards_per_page'] > 0
        assert sample_config['scale_factor'] > 0
        assert sample_config['bead_shape'] in ['diamond', 'circle', 'square']
        assert sample_config['color_scheme'] in ['monochrome', 'place-value', 'heaven-earth', 'alternating']