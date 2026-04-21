#!/bin/bash
# Quick test script for Snake Game

echo "=== Snake Game Test ==="
echo ""

# Check Python version
echo "1. Checking Python version..."
python3 --version

echo ""
echo "2. Checking dependencies..."
pip3 list | grep -E "(pygame|pytest)" || echo "Installing dependencies..."

echo ""
echo "3. Running tests..."
cd ~/projects/snake-game
python3 -m pytest tests/ -v

echo ""
echo "4. Testing game import..."
python3 -c "
import sys
sys.path.insert(0, '.')
try:
    from src.game import SnakeGame
    print('✓ Game imports successfully')
    print('✓ All modules loaded correctly')
except Exception as e:
    print(f'✗ Import failed: {e}')
"

echo ""
echo "=== Setup Complete ==="
echo "To run the game:"
echo "  cd ~/projects/snake-game"
echo "  python3 run.py"
echo ""
echo "Or install as package:"
echo "  pip3 install -e ."
echo "  snake-game"
echo ""
echo "Repository: https://github.com/se4n-d0m1n1c/snake-game"