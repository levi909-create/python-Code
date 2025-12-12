"""
Python Code - A Collection of Python Learning Projects

This package contains various Python modules demonstrating:
- Poetry management and analysis (poets)
- Mathematical operations and string manipulation utilities (codes_for_fun)
- Random number generation and visualization (random_range)
"""

__version__ = "1.0.0"
__author__ = "Levi"

# Import main modules for easy access
from . import poets
from . import codes_for_fun
from . import random_range

__all__ = ['poets', 'codes_for_fun', 'random_range']
