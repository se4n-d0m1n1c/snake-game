#!/usr/bin/env python3
"""
Test to verify difficulty levels are correctly ordered.
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.config import DIFFICULTY_SPEEDS

def test_difficulty_levels():
    """Test that difficulty levels are correctly ordered (easy = slowest, hard = fastest)."""
    print("Testing difficulty levels...")
    print(f"DIFFICULTY_SPEEDS = {DIFFICULTY_SPEEDS}")
    print()
    
    # Easy should have the highest number (slowest)
    easy_speed = DIFFICULTY_SPEEDS["easy"]
    medium_speed = DIFFICULTY_SPEEDS["medium"]
    hard_speed = DIFFICULTY_SPEEDS["hard"]
    
    print(f"Easy:   {easy_speed} frames per move")
    print(f"Medium: {medium_speed} frames per move")
    print(f"Hard:   {hard_speed} frames per move")
    print()
    
    # Verify ordering: easy > medium > hard (higher = slower = easier)
    if easy_speed > medium_speed > hard_speed:
        print("✓ PASS: Difficulty levels are correctly ordered!")
        print("  Easy is slowest (easiest)")
        print("  Medium is medium speed")
        print("  Hard is fastest (hardest)")
        return True
    else:
        print("✗ FAIL: Difficulty levels are incorrectly ordered!")
        print("  Expected: easy > medium > hard")
        print(f"  Got: easy={easy_speed}, medium={medium_speed}, hard={hard_speed}")
        return False

def explain_speed_mechanic():
    """Explain how the speed mechanic works."""
    print("\n" + "="*60)
    print("HOW SPEED WORKS:")
    print("="*60)
    print("The game runs at 60 FPS (frames per second).")
    print("The 'speed' value is 'frames per move'.")
    print()
    print("Examples:")
    print(f"  Easy ({DIFFICULTY_SPEEDS['easy']} frames/move):")
    print(f"    Snake moves every {DIFFICULTY_SPEEDS['easy']} frames")
    print(f"    ≈ {60/DIFFICULTY_SPEEDS['easy']:.1f} moves per second")
    print()
    print(f"  Medium ({DIFFICULTY_SPEEDS['medium']} frames/move):")
    print(f"    Snake moves every {DIFFICULTY_SPEEDS['medium']} frames")
    print(f"    ≈ {60/DIFFICULTY_SPEEDS['medium']:.1f} moves per second")
    print()
    print(f"  Hard ({DIFFICULTY_SPEEDS['hard']} frames/move):")
    print(f"    Snake moves every {DIFFICULTY_SPEEDS['hard']} frames")
    print(f"    ≈ {60/DIFFICULTY_SPEEDS['hard']:.1f} moves per second")
    print()
    print("Higher frames/move = slower snake = easier game")
    print("Lower frames/move = faster snake = harder game")

if __name__ == "__main__":
    success = test_difficulty_levels()
    explain_speed_mechanic()
    sys.exit(0 if success else 1)