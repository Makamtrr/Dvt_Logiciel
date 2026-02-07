"""Pytest configuration file."""

import sys
from pathlib import Path

# Add src directory to Python path (absolute path)
src_path = Path(__file__).parent.parent / "src"
abs_src_path = src_path.resolve()

if str(abs_src_path) not in sys.path:
    sys.path.insert(0, str(abs_src_path))

print(f"Added to PYTHONPATH: {abs_src_path}")
