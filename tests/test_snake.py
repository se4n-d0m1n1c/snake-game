"""
Test module for Snake class.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from snake import Snake
from config import *


def test_snake_initialization():
    """Test snake initialization."""
    snake = Snake()
    assert len(snake.positions) == INITIAL_SNAKE_LENGTH
    assert snake.direction == DIRECTION_RIGHT
    assert snake.alive == True
    assert snake.score == 0
    print("✓ Snake initialization test passed")


def test_snake_movement():
    """Test snake movement."""
    snake = Snake(start_pos=(5, 5))
    initial_head = snake.get_head_position()
    
    # Move right
    snake.move()
    new_head = snake.get_head_position()
    assert new_head == (6, 5)
    
    # Change direction and move
    snake.change_direction(DIRECTION_DOWN)
    snake.move()
    assert snake.get_head_position() == (6, 6)
    print("✓ Snake movement test passed")


def test_snake_growth():
    """Test snake growth when eating food."""
    snake = Snake(start_pos=(5, 5), start_length=3)
    initial_length = len(snake.positions)
    
    # Grow snake
    snake.grow(2)
    
    # Move enough times to see the growth
    for _ in range(10):
        snake.move()
    
    # Snake should have grown by 2 segments
    assert snake.score == FOOD_SCORE_VALUE * 2
    print("✓ Snake growth test passed")


def test_snake_collision():
    """Test snake self-collision detection."""
    snake = Snake(start_pos=(5, 5), start_length=3)
    
    # Create a situation where snake collides with itself
    # by making it turn into itself
    snake.change_direction(DIRECTION_DOWN)
    snake.move()  # Head at (5, 6)
    
    snake.change_direction(DIRECTION_LEFT)
    snake.move()  # Head at (4, 6)
    
    snake.change_direction(DIRECTION_UP)
    snake.move()  # Head at (4, 5)
    
    snake.change_direction(DIRECTION_RIGHT)
    snake.move()  # Head at (5, 5) - collides with original tail position
    
    # Snake should be dead
    assert snake.alive == False
    print("✓ Snake collision test passed")


def test_boundary_wrapping():
    """Test that snake wraps around screen boundaries."""
    snake = Snake(start_pos=(GRID_WIDTH - 1, GRID_HEIGHT // 2))
    
    # Move right at right edge - should wrap to left
    snake.move()
    head = snake.get_head_position()
    assert head[0] == 0  # Wrapped from right edge to left edge
    print("✓ Boundary wrapping test passed")


if __name__ == "__main__":
    print("Running Snake tests...")
    test_snake_initialization()
    test_snake_movement()
    test_snake_growth()
    test_snake_collision()
    test_boundary_wrapping()
    print("\nAll tests passed!")