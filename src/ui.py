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
        score_bg = pygame.Surface((SCREEN_WIDTH, UI_HEIGHT), pygame.SRCALPHA)
        score_bg.fill(UI_BACKGROUND)
        self.screen.blit(score_bg, (0, 0))
        
        # Draw scores
        self.draw_text(f"Score: {score}", "normal", UI_TEXT_COLOR, 20, 20)
        self.draw_text(f"High Score: {high_score}", "normal", UI_ACCENT_COLOR, 20, 50)
        
        # Draw difficulty - positioned from right edge (shows selected difficulty)
        difficulty_text = f"Difficulty: {difficulty.capitalize()}"
        difficulty_font = self.fonts.get("normal", self.fonts["normal"])
        difficulty_width = difficulty_font.size(difficulty_text)[0]
        self.draw_text(difficulty_text, "normal", UI_TEXT_COLOR, 
                      SCREEN_WIDTH - difficulty_width - 20, 20)
        
        # Draw controls hint - positioned from right edge
        controls_text = "P: Pause | R: Menu | ESC: Quit"
        controls_font = self.fonts.get("small", self.fonts["normal"])
        controls_width = controls_font.size(controls_text)[0]
        self.draw_text(controls_text, "small", UI_TEXT_COLOR,
                      SCREEN_WIDTH - controls_width - 20, 50)
    
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
        self.draw_text("Press R to return to menu", "small", UI_TEXT_COLOR,
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60, center=True)
        self.draw_text("Press ESC to quit", "small", UI_TEXT_COLOR,
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, center=True)
    
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
        
        # Draw return to menu instructions
        self.draw_text("Press R to return to menu", "normal", UI_TEXT_COLOR,
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80, center=True)
        self.draw_text("Press ESC to quit", "small", UI_TEXT_COLOR,
                      SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120, center=True)
    
    def draw_grid(self) -> None:
        """Draw the game grid (only in the game area below UI)."""
        # Draw vertical lines (full height of game area)
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, 
                           (x, GAME_AREA_TOP), 
                           (x, SCREEN_HEIGHT), 1)
        
        # Draw horizontal lines (only in game area)
        for y in range(GAME_AREA_TOP, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, 
                           (0, y), 
                           (SCREEN_WIDTH, y), 1)
    
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
    
    def draw_menu(self, selected_difficulty: str, high_score: int, menu_state: str = "main") -> None:
        """
        Draw the main menu screen.
        
        Args:
            selected_difficulty: Currently selected difficulty.
            high_score: Current high score.
            menu_state: "main" for play button, "difficulty" for difficulty selection
        """
        # Draw background
        self.screen.fill(BACKGROUND_COLOR)
        
        if menu_state == "main":
            # Draw animated title (centered at top)
            title_y = self._get_title_y_position()
            self.draw_text("SNAKE GAME", "title", UI_ACCENT_COLOR,
                          SCREEN_WIDTH // 2, title_y, center=True)
            
            # Calculate vertical center for main menu content
            content_start_y = SCREEN_HEIGHT // 2 - 100
            
            # Draw high score (centered)
            self.draw_text(f"High Score: {high_score}", "heading", UI_TEXT_COLOR,
                          SCREEN_WIDTH // 2, content_start_y, center=True)
            
            # Draw play button (below high score)
            self.draw_text("PRESS ENTER TO PLAY", "heading", UI_ACCENT_COLOR,
                          SCREEN_WIDTH // 2, content_start_y + 100, center=True)
            
            # Draw instructions at bottom
            self.draw_text("Press ESC to quit", "small", UI_TEXT_COLOR,
                          SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80, center=True)
            
        elif menu_state == "difficulty":
            # Calculate vertical center for difficulty selection content
            # Perfectly center the 3 options around screen center
            content_start_y = SCREEN_HEIGHT // 2 - 160
            
            # Draw difficulty selection title
            self.draw_text("SELECT DIFFICULTY", "heading", UI_TEXT_COLOR,
                          SCREEN_WIDTH // 2, content_start_y, center=True)
            
            # Draw difficulty options
            difficulties = [
                ("EASY", "1", "easy"),
                ("MEDIUM", "2", "medium"),
                ("HARD", "3", "hard")
            ]
            
            y_offset = content_start_y + 80
            option_spacing = 80
            
            for name, key, difficulty in difficulties:
                # Highlight selected difficulty
                color = UI_ACCENT_COLOR if difficulty == selected_difficulty else UI_TEXT_COLOR
                
                # Draw option
                option_text = f"{name} (Press {key})"
                self.draw_text(option_text, "normal", color,
                              SCREEN_WIDTH // 2, y_offset, center=True)
                
                y_offset += option_spacing
            
            # Draw instructions at bottom
            self.draw_text("Press ESC to go back", "small", UI_TEXT_COLOR,
                          SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80, center=True)
    
    def _get_title_y_position(self) -> int:
        """Calculate animated title Y position with bobbing effect."""
        import time
        import math
        # Smooth bobbing animation: sin wave with 2 second period, 10 pixel amplitude
        current_time = time.time()
        bob_offset = int(10 * math.sin(current_time * 3.14))  # Smooth sin wave
        return 80 + bob_offset  # Start at 80, bob up and down