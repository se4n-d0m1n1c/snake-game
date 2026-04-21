"""
Snake Class

This module defines the Snake class which handles the snake's movement,
growth, collision detection, and rendering.
"""

import pygame
from typing import List, Tuple
from .config import *


class Snake:
    """Represents the snake in the game."""
    
    def __init__(self, start_pos: Tuple[int, int] = None, start_length: int = INITIAL_SNAKE_LENGTH):
        """
        Initialize the snake.
        
        Args:
            start_pos: Starting position (x, y) in grid coordinates. 
                      If None, starts at center of grid.
            start_length: Initial length of the snake.
        """
        if start_pos is None:
            start_pos = (GRID_WIDTH // 2, GRID_HEIGHT // 2)
            
        self.positions = [start_pos]
        self.direction = DIRECTION_RIGHT
        self.next_direction = self.direction
        self.length = start_length
        self.grow_pending = start_length - 1
        self.alive = True
        self.score = 0
        
        # Initialize snake body
        for i in range(1, start_length):
            self.positions.append((start_pos[0] - i, start_pos[1]))
    
    def change_direction(self, new_direction: Tuple[int, int]) -> None:
        """
        Change the snake's direction for the next move.
        
        Args:
            new_direction: New direction vector (dx, dy)
        """
        # Prevent 180-degree turns (can't go directly opposite)
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.next_direction = new_direction
    
    def move(self) -> None:
        """
        Move the snake one step in its current direction.
        """
        # Update direction
        self.direction = self.next_direction
        
        # Calculate new head position
        head_x, head_y = self.positions[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)
        
        # Check for collision with self
        if new_head in self.positions:
            self.alive = False
            return
        
        # Add new head
        self.positions.insert(0, new_head)
        
        # Remove tail if not growing
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.positions.pop()
    
    def grow(self, amount: int = 1) -> None:
        """
        Make the snake grow by the specified amount.
        
        Args:
            amount: Number of segments to grow.
        """
        self.grow_pending += amount
        self.score += FOOD_SCORE_VALUE * amount
    
    def get_head_position(self) -> Tuple[int, int]:
        """
        Get the current position of the snake's head.
        
        Returns:
            Tuple of (x, y) grid coordinates.
        """
        return self.positions[0]
    
    def get_body_positions(self) -> List[Tuple[int, int]]:
        """
        Get all body positions (excluding head).
        
        Returns:
            List of (x, y) grid coordinates.
        """
        return self.positions[1:]
    
    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the snake on the given surface.
        
        Args:
            surface: PyGame surface to draw on.
        """
        for i, (x, y) in enumerate(self.positions):
            # Calculate pixel coordinates (adjust for game area offset)
            rect = pygame.Rect(
                x * GRID_SIZE, 
                y * GRID_SIZE + GAME_AREA_TOP, 
                GRID_SIZE, 
                GRID_SIZE
            )
            
            # Draw snake segment
            if i == 0:  # Head
                color = SNAKE_HEAD_COLOR
            else:  # Body
                # Slight color variation for body segments
                color_variation = min(50, i * 2)
                color = (
                    max(0, SNAKE_BODY_COLOR[0] - color_variation),
                    max(0, SNAKE_BODY_COLOR[1] - color_variation),
                    max(0, SNAKE_BODY_COLOR[2] - color_variation)
                )
            
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, SNAKE_OUTLINE_COLOR, rect, 1)
            
            # Draw eyes on head
            if i == 0:
                eye_size = GRID_SIZE // 5
                # Calculate eye positions based on direction
                if self.direction == DIRECTION_RIGHT:
                    left_eye = (rect.right - eye_size * 2, rect.top + eye_size * 2)
                    right_eye = (rect.right - eye_size * 2, rect.bottom - eye_size * 2)
                elif self.direction == DIRECTION_LEFT:
                    left_eye = (rect.left + eye_size, rect.top + eye_size * 2)
                    right_eye = (rect.left + eye_size, rect.bottom - eye_size * 2)
                elif self.direction == DIRECTION_UP:
                    left_eye = (rect.left + eye_size * 2, rect.top + eye_size)
                    right_eye = (rect.right - eye_size * 2, rect.top + eye_size)
                else:  # DOWN
                    left_eye = (rect.left + eye_size * 2, rect.bottom - eye_size)
                    right_eye = (rect.right - eye_size * 2, rect.bottom - eye_size)
                
                pygame.draw.circle(surface, (0, 0, 0), left_eye, eye_size)
                pygame.draw.circle(surface, (0, 0, 0), right_eye, eye_size)