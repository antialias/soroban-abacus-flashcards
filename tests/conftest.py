"""Pytest configuration and fixtures for soroban flashcard tests."""

import pytest
import tempfile
import shutil
from pathlib import Path

# Add src to path for importing
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

@pytest.fixture
def temp_dir():
    """Create a temporary directory for test outputs."""
    temp_path = Path(tempfile.mkdtemp())
    yield temp_path
    shutil.rmtree(temp_path)

@pytest.fixture
def project_root():
    """Get the project root directory."""
    return Path(__file__).parent.parent

@pytest.fixture
def sample_config():
    """Basic test configuration."""
    return {
        'range': '0-9',
        'cards_per_page': 6,
        'paper_size': 'us-letter',
        'orientation': 'portrait',
        'bead_shape': 'diamond',
        'color_scheme': 'monochrome',
        'font_family': 'DejaVu Sans',
        'font_size': '48pt',
        'scale_factor': 0.9,
        'margins': {
            'top': '0.5in',
            'bottom': '0.5in',
            'left': '0.5in',
            'right': '0.5in'
        },
        'gutter': '5mm'
    }

@pytest.fixture
def reference_images_dir(project_root):
    """Directory containing reference images for visual tests."""
    ref_dir = project_root / 'tests' / 'references'
    ref_dir.mkdir(exist_ok=True)
    return ref_dir

