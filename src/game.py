"""
Main Game Module

This is the main entry point for the Snake game.
Handles the game loop, state management, and coordination between modules.
"""

import pygame
import sys
import os
from typing import Optional
from .snake import Snake
from .food import Food
from .ui import UI
from .audio import AudioManager
from .config import *


class SnakeGame:
    """Main game controller class."""
    
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        
        # Set up display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        
        # Set up game clock
        self.clock = pygame.time.Clock()
        
        # Initialize game components
        self.ui = UI(self.screen)
        self.audio = AudioManager()
        self.high_score = self._load_high_score()
        
        # Game state
        self.state = STATE_MENU  # Start in menu state
        self.menu_state = "main"  # "main" or "difficulty"
        self.difficulty = "medium"  # Default difficulty
        self.speed = DIFFICULTY_SPEEDS[self.difficulty]
        self.move_counter = 0
        self.difficulty_notification_timer = 0
        
        # Initialize game objects (but don't start game yet)
        self.snake = None
        self.food = None
        self.score = 0
        
        # Start background music
        self.audio.play_background_music()
    
    def _load_high_score(self) -> int:
        """
        Load the high score from file.
        
        Returns:
            High score (0 if file doesn't exist).
        """
        try:
            if os.path.exists(HIGH_SCORE_FILE):
                with open(HIGH_SCORE_FILE, 'r') as f:
                    return int(f.read().strip())
        except:
            pass
        return 0
    
    def _save_high_score(self) -> None:
        """Save the high score to file."""
        try:
            with open(HIGH_SCORE_FILE, 'w') as f:
                f.write(str(self.high_score))
        except:
            pass  # Silently fail if save fails
    
    def reset_game(self) -> None:
        """Reset the game to initial state."""
        self.snake = Snake()
        self.food = Food(self.snake.positions)
        self.score = 0
        self.state = STATE_PLAYING
        self.move_counter = 0
    
    def start_game(self) -> None:
        """Start the game with selected difficulty."""
        self.reset_game()
        self.audio.resume_background_music()
    
    def return_to_menu(self) -> None:
        """Return to main menu."""
        self.state = STATE_MENU
        self.menu_state = "main"  # Reset to main menu
        self.snake = None
        self.food = None
        self.score = 0
        self.audio.stop_background_music()
        self.audio.play_background_music()
    
    def handle_events(self) -> None:
        """Handle PyGame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)
    
    def handle_keydown(self, key: int) -> None:
        """
        Handle key press events.
        
        Args:
            key: PyGame key constant.
        """
        if self.state == STATE_MENU:
            if self.menu_state == "main":
                # Main menu controls
                if key == pygame.K_RETURN or key == pygame.K_SPACE:
                    # Enter or Space to go to difficulty selection
                    self.menu_state = "difficulty"
                elif key == KEY_QUIT:
                    self.quit_game()
                    
            elif self.menu_state == "difficulty":
                # Difficulty selection controls
                if key == KEY_EASY:
                    self.difficulty = "easy"
                    self.speed = DIFFICULTY_SPEEDS["easy"]
                    self.start_game()
                elif key == KEY_MEDIUM:
                    self.difficulty = "medium"
                    self.speed = DIFFICULTY_SPEEDS["medium"]
                    self.start_game()
                elif key == KEY_HARD:
                    self.difficulty = "hard"
                    self.speed = DIFFICULTY_SPEEDS["hard"]
                    self.start_game()
                elif key == KEY_QUIT:
                    # ESC goes back to main menu
                    self.menu_state = "main"
                
        elif self.state == STATE_PLAYING:
            # Direction controls only during gameplay
            if key == KEY_UP:
                self.snake.change_direction(DIRECTION_UP)
                self.audio.play_move_sound()
            elif key == KEY_DOWN:
                self.snake.change_direction(DIRECTION_DOWN)
                self.audio.play_move_sound()
            elif key == KEY_LEFT:
                self.snake.change_direction(DIRECTION_LEFT)
                self.audio.play_move_sound()
            elif key == KEY_RIGHT:
                self.snake.change_direction(DIRECTION_RIGHT)
                self.audio.play_move_sound()
        
        # Global controls (work in all states except menu for some)
        if key == KEY_PAUSE and self.state == STATE_PLAYING:
            self.toggle_pause()
        elif key == KEY_RESTART and self.state in [STATE_PLAYING, STATE_PAUSED, STATE_GAME_OVER]:
            self.return_to_menu()
        elif key == KEY_QUIT and self.state != STATE_MENU:
            self.return_to_menu()
    
    def toggle_pause(self) -> None:
        """Toggle between paused and playing states."""
        if self.state == STATE_PLAYING:
            self.state = STATE_PAUSED
            self.audio.pause_background_music()
        elif self.state == STATE_PAUSED:
            self.state = STATE_PLAYING
            self.audio.resume_background_music()
    
    def update(self) -> None:
        """Update game state."""
        if self.state != STATE_PLAYING:
            return
        
        # Update move counter
        self.move_counter += 1
        if self.move_counter >= self.speed:
            self.move_counter = 0
            
            # Move snake
            self.snake.move()
            
            # Check for food collision
            if self.food.check_collision(self.snake.get_head_position()):
                self.snake.grow()
                self.food.respawn(self.snake.positions)
                self.audio.play_eat_sound()
                
                # Update score and high score
                self.score = self.snake.score
                if self.score > self.high_score:
                    self.high_score = self.score
                    self._save_high_score()
            
            # Check for game over
            if not self.snake.alive:
                self.state = STATE_GAME_OVER
                self.audio.play_game_over_sound()
                self.audio.stop_background_music()
        
        # Update food animation
        if self.food:
            self.food.update()
        
        # Update difficulty notification timer
        if self.difficulty_notification_timer > 0:
            self.difficulty_notification_timer -= 1
    
    def draw(self) -> None:
        """Draw the game."""
        # Clear screen with different colors for UI and game areas
        self.screen.fill(UI_BACKGROUND[:3])  # UI area background (solid color)
        
        if self.state == STATE_MENU:
            # Draw menu screen
            self.ui.draw_menu(self.difficulty, self.high_score, self.menu_state)
        else:
            # Draw game area background
            game_area_bg = pygame.Rect(0, GAME_AREA_TOP, SCREEN_WIDTH, GAME_AREA_HEIGHT)
            pygame.draw.rect(self.screen, BACKGROUND_COLOR, game_area_bg)
            
            # Draw grid
            self.ui.draw_grid()
            
            # Draw game objects if they exist
            if self.snake:
                self.snake.draw(self.screen)
            if self.food:
                self.food.draw(self.screen)
            
            # Draw UI elements (semi-transparent overlay)
            self.ui.draw_score(self.score, self.high_score, self.difficulty)
            
            # Draw difficulty notification if active
            if self.difficulty_notification_timer > 0:
                self.ui.draw_difficulty_change(self.difficulty)
            
            # Draw state-specific overlays
            if self.state == STATE_PAUSED:
                self.ui.draw_pause_screen()
            elif self.state == STATE_GAME_OVER:
                self.ui.draw_game_over(self.score, self.high_score)
        
        # Update display
        pygame.display.flip()
    
    def run(self) -> None:
        """Main game loop."""
        try:
            while True:
                self.handle_events()
                self.update()
                self.draw()
                self.clock.tick(ANIMATION_FPS)
        except KeyboardInterrupt:
            self.quit_game()
    
    def quit_game(self) -> None:
        """Clean up and quit the game."""
        self._save_high_score()
        self.audio.cleanup()
        pygame.quit()
        sys.exit()


def main():
    """Entry point for the game."""
    game = SnakeGame()
    game.run()


if __name__ == "__main__":
    main()