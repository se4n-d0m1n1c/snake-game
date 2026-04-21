"""
Food Class

This module defines the Food class which handles food generation,
collision detection, and rendering.
"""

import pygame
import random
from typing import Tuple, List
from .config import *


class Food:
    """Represents the food that the snake eats."""
    
    def __init__(self, snake_positions: List[Tuple[int, int]] = None):
        """
        Initialize food at a random position.
        
        Args:
            snake_positions: List of positions occupied by the snake
                           (to avoid spawning on snake).
        """
        if snake_positions is None:
            snake_positions = []
        
        self.position = self._generate_position(snake_positions)
        self.glow_phase = 0  # For pulsing animation
        self.eaten = False
    
    def _generate_position(self, snake_positions: List[Tuple[int, int]]) -> Tuple[int, int]:
        """
        Generate a random position not occupied by the snake.
        
        Args:
            snake_positions: List of positions to avoid.
            
        Returns:
            Random (x, y) grid coordinates.
        """
        while True:
            position = (
                random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1)
            )
            if position not in snake_positions:
                return position
    
    def check_collision(self, snake_head: Tuple[int, int]) -> bool:
        """
        Check if the snake's head has collided with the food.
        
        Args:
            snake_head: Position of snake's head.
            
        Returns:
            True if collision detected.
        """
        return snake_head == self.position
    
    def respawn(self, snake_positions: List[Tuple[int, int]]) -> None:
        """
        Respawn food at a new random position.
        
        Args:
            snake_positions: List of positions to avoid.
        """
        self.position = self._generate_position(snake_positions)
        self.eaten = False
    
    def update(self) -> None:
        """Update food animation."""
        self.glow_phase = (self.glow_phase + 0.1) % (2 * 3.14159)
    
    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the food on the given surface.
        
        Args:
            surface: PyGame surface to draw on.
        """
        # Calculate pixel coordinates
        x, y = self.position
        center_x = x * GRID_SIZE + GRID_SIZE // 2
        center_y = y * GRID_SIZE + GRID_SIZE // 2
        
        # Calculate pulsing glow effect
        glow_intensity = 0.5 + 0.5 * abs(pygame.math.Vector2(1, 0).rotate(self.glow_phase * 50).x)
        glow_radius = int(GRID_SIZE * 0.7 * glow_intensity)
        
        # Draw glow effect
        glow_color = (
            min(255, int(FOOD_GLOW_COLOR[0] * glow_intensity)),
            min(255, int(FOOD_GLOW_COLOR[1] * glow_intensity)),
            min(255, int(FOOD_GLOW_COLOR[2] * glow_intensity))
        )
        
        # Draw outer glow
        for radius in range(glow_radius, 0, -2):
            alpha = int(50 * (radius / glow_radius))
            if alpha > 0:
                glow_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(
                    glow_surface, 
                    (*glow_color, alpha), 
                    (radius, radius), 
                    radius
                )
                surface.blit(
                    glow_surface, 
                    (center_x - radius, center_y - radius), 
                    special_flags=pygame.BLEND_ALPHA_SDL2
                )
        
        # Draw main food circle
        food_radius = GRID_SIZE // 3
        pygame.draw.circle(
            surface, 
            FOOD_COLOR, 
            (center_x, center_y), 
            food_radius
        )
        
        # Draw highlight
        highlight_radius = food_radius // 3
        highlight_pos = (
            center_x - highlight_radius // 2,
            center_y - highlight_radius // 2
        )
        pygame.draw.circle(
            surface, 
            (255, 255, 255, 150), 
            highlight_pos, 
            highlight_radius
        )