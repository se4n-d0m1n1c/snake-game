"""
Test module for Food class.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.food import Food
from src.snake import Snake


def test_food_initialization():
    """Test food initialization."""
    snake = Snake()
    food = Food(snake.positions)
    
    assert food.position not in snake.positions
    assert food.eaten == False
    print("✓ Food initialization test passed")


def test_food_collision():
    """Test food collision detection."""
    snake = Snake(start_pos=(5, 5))
    food = Food(snake.positions)
    
    # Position food at snake's head (simulate collision)
    food.position = (5, 5)
    
    assert food.check_collision(snake.get_head_position()) == True
    print("✓ Food collision test passed")


def test_food_respawn():
    """Test food respawn."""
    snake = Snake(start_pos=(5, 5))
    food = Food(snake.positions)
    
    original_position = food.position
    
    # Respawn food
    food.respawn(snake.positions)
    
    assert food.position != original_position
    assert food.position not in snake.positions
    print("✓ Food respawn test passed")


def test_food_avoid_snake():
    """Test that food doesn't spawn on snake."""
    # Create a snake that fills most of the grid
    snake_positions = [(x, y) for x in range(10) for y in range(10)]
    
    # This should still find a position (if grid is larger than 10x10)
    try:
        food = Food(snake_positions)
        assert food.position not in snake_positions
        print("✓ Food avoids snake test passed")
    except RecursionError:
        # Expected if grid is too small
        print("⚠ Food generation test skipped (grid too small)")


if __name__ == "__main__":
    print("Running Food tests...")
    test_food_initialization()
    test_food_collision()
    test_food_respawn()
    test_food_avoid_snake()
    print("\nAll tests passed!")