#!/usr/bin/env python3
"""
Simple run script for the Snake Game.
"""

import sys
import os

# Add current directory to path for module resolution
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Now import from src
from src.game import main

if __name__ == "__main__":
    main()