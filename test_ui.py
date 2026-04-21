#!/usr/bin/env python3
"""
Quick visual test for UI positioning fix.
"""

import pygame
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.ui import UI
from src.config import *

def test_ui_positioning():
    """Test that UI elements are properly positioned."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("UI Positioning Test")
    
    ui = UI(screen)
    
    # Test with different scores and difficulties
    test_cases = [
        (0, 0, "easy"),
        (150, 1000, "medium"),
        (999, 9999, "hard"),
    ]
    
    clock = pygame.time.Clock()
    running = True
    test_index = 0
    
    while running and test_index < len(test_cases):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    test_index += 1
                elif event.key == pygame.K_ESCAPE:
                    running = False
        
        if test_index >= len(test_cases):
            break
            
        score, high_score, difficulty = test_cases[test_index]
        
        # Clear screen
        screen.fill(BACKGROUND_COLOR)
        
        # Draw UI
        ui.draw_score(score, high_score, difficulty)
        
        # Draw test info
        font = pygame.font.SysFont(FONT_NAME, 20)
        info_text = f"Test {test_index + 1}/{len(test_cases)}: Score={score}, High={high_score}, Diff={difficulty}"
        info_surface = font.render(info_text, True, (255, 255, 255))
        screen.blit(info_surface, (10, SCREEN_HEIGHT - 40))
        
        instruction = "Press SPACE for next test, ESC to quit"
        instruction_surface = font.render(instruction, True, (200, 200, 200))
        screen.blit(instruction_surface, (10, SCREEN_HEIGHT - 20))
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    print("UI positioning test completed.")
    print("Check that all text fits within screen boundaries.")
    print("Right-aligned text should have 20px padding from right edge.")

if __name__ == "__main__":
    test_ui_positioning()