#!/usr/bin/env python3
"""
Simple run script for the Snake Game.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from game import main

if __name__ == "__main__":
    main()