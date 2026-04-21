"""
User Interface Module

This module handles all UI rendering including score display,
game over screens, pause screens, and text rendering.
"""

import pygame
from typing import Optional
from .config import *


class UI:
    """Handles all user interface rendering."""
    
    def __init__(self, screen: pygame.Surface):
        """
        Initialize the UI renderer.
        
        Args:
            screen: PyGame surface to draw on.
        """
        self.screen = screen
        self.fonts = self._load_fonts()
        
    def _load_fonts(self) -> dict:
        """
        Load all required fonts.
        
        Returns:
            Dictionary of font sizes to font objects.
        """
        fonts = {}
        try:
            for size_name, size in FONT_SIZES.items():
                fonts[size_name] = pygame.font.SysFont(FONT_NAME, size)
        except:
            # Fallback to default font if specified font not available
            for size_name, size in FONT_SIZES.items():
                fonts[size_name] = pygame.font.Font(None, size)
        return fonts
    
    def draw_text(self, text: str, size: str, color: tuple, 
                  x: int, y: int, center: bool = False) -> None:
        """
        Draw text on the screen.
        
        Args:
            text: Text to display.
            size: Font size key (e.g., "title", "normal").
            color: RGB color tuple.
            x: X coordinate.
            y: Y coordinate.
            center: If True, center the text at (x, y).
        """
        font = self.fonts.get(size, self.fonts["normal"])
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        
        if center:
            text_rect.center = (x, y)
        else:
            text_rect.topleft = (x, y)
            
        self.screen.blit(text_surface, text_rect)
    
    def draw_score(self, score: int, high_score: int, difficulty: str) -> None:
        """
        Draw the score display.
        
        Args:
            score: Current score.
            high_score: High score.
            difficulty: Current difficulty level.
        """
        # Draw semi-transparent background
        score_bg = pygame.Surface((SCREEN_WIDTH, 60), pygame.SRCALPHA)
        score_bg.fill(UI_BACKGROUND)
        self.screen.blit(score_bg, (0, 0))
        
        # Draw scores
        self.draw_text(f"Score: {score}", "normal", UI_TEXT_COLOR, 20, 15)
        self.draw_text(f"High Score: {high_score}", "normal", UI_ACCENT_COLOR, 20, 45)
        
        # Draw difficulty
        difficulty_text = f"Difficulty: {difficulty.capitalize()}"
        self.draw_text(difficulty_text, "normal", UI_TEXT_COLOR, SCREEN_WIDTH - 200, 15)
        
        # Draw controls hint
        controls_text = "P: Pause | R: Restart | ESC: Quit"
        self.draw_text(controls_text, "small", UI_TEXT_COLOR, SCREEN_WIDTH - 200, 45)
    
    def draw_pause_screen(self) -> None:
        """Draw the pause screen overlay."""
        # Draw semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))
        
        # Draw pause text
        self.draw_text("PAUSED", "title", UI_ACCENT_COLOR, 
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, center=True)
        self.draw_text("Press P to resume", "normal", UI_TEXT_COLOR,
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20, center=True)
        self.draw_text("Press ESC to quit", "small", UI_TEXT_COLOR,
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60, center=True)
    
    def draw_game_over(self, score: int, high_score: int) -> None:
        """
        Draw the game over screen.
        
        Args:
            score: Final score.
            high_score: High score.
        """
        # Draw semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))
        
        # Draw game over text
        self.draw_text("GAME OVER", "title", UI_WARNING_COLOR,
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, center=True)
        
        # Draw score information
        self.draw_text(f"Your Score: {score}", "heading", UI_TEXT_COLOR,
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20, center=True)
        
        if score == high_score and score > 0:
            self.draw_text("NEW HIGH SCORE!", "normal", UI_ACCENT_COLOR,
                          SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20, center=True)
        else:
            self.draw_text(f"High Score: {high_score}", "normal", UI_TEXT_COLOR,
                          SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20, center=True)
        
        # Draw restart instructions
        self.draw_text("Press R to restart", "normal", UI_TEXT_COLOR,
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80, center=True)
        self.draw_text("Press ESC to quit", "small", UI_TEXT_COLOR,
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120, center=True)
    
    def draw_grid(self) -> None:
        """Draw the game grid."""
        # Draw vertical lines
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT), 1)
        
        # Draw horizontal lines
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y), 1)
    
    def draw_difficulty_change(self, difficulty: str) -> None:
        """
        Draw a temporary difficulty change notification.
        
        Args:
            difficulty: New difficulty level.
        """
        # Create notification surface
        notification = pygame.Surface((300, 60), pygame.SRCALPHA)
        notification.fill((*UI_ACCENT_COLOR[:3], 200))
        
        # Draw border
        pygame.draw.rect(notification, UI_TEXT_COLOR, notification.get_rect(), 2)
        
        # Draw text
        font = self.fonts["normal"]
        text = font.render(f"Difficulty: {difficulty.capitalize()}", True, UI_TEXT_COLOR)
        text_rect = text.get_rect(center=(150, 30))
        notification.blit(text, text_rect)
        
        # Position and draw notification
        notification_rect = notification.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
        )
        self.screen.blit(notification, notification_rect)