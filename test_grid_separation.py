#!/usr/bin/env python3
"""
Visual test for grid separation from UI.
"""

import pygame
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.config import *
from src.ui import UI

def test_grid_separation():
    """Test that grid is properly separated from UI area."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Grid Separation Test")
    
    ui = UI(screen)
    clock = pygame.time.Clock()
    
    print("Testing grid separation...")
    print(f"Screen: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    print(f"UI Height: {UI_HEIGHT}px")
    print(f"Game Area Top: {GAME_AREA_TOP}px")
    print(f"Game Area Height: {GAME_AREA_HEIGHT}px")
    print(f"Grid Cells: {GRID_WIDTH}x{GRID_HEIGHT}")
    print()
    
    # Calculate expected grid boundaries
    expected_grid_top = GAME_AREA_TOP
    expected_grid_bottom = SCREEN_HEIGHT
    expected_grid_left = 0
    expected_grid_right = SCREEN_WIDTH
    
    print(f"Expected grid boundaries:")
    print(f"  Top: {expected_grid_top}px (below UI)")
    print(f"  Bottom: {expected_grid_bottom}px")
    print(f"  Left: {expected_grid_left}px")
    print(f"  Right: {expected_grid_right}px")
    print()
    
    # Draw test visualization
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Clear screen
        screen.fill((0, 0, 0))
        
        # Draw UI area (different color)
        ui_area = pygame.Rect(0, 0, SCREEN_WIDTH, UI_HEIGHT)
        pygame.draw.rect(screen, (40, 40, 60), ui_area)  # Dark blue for UI area
        
        # Draw game area (different color)
        game_area = pygame.Rect(0, GAME_AREA_TOP, SCREEN_WIDTH, GAME_AREA_HEIGHT)
        pygame.draw.rect(screen, (20, 20, 40), game_area)  # Darker blue for game area
        
        # Draw grid
        ui.draw_grid()
        
        # Draw boundary lines
        # UI/Game boundary (red line)
        pygame.draw.line(screen, (255, 0, 0), (0, GAME_AREA_TOP), (SCREEN_WIDTH, GAME_AREA_TOP), 3)
        
        # Draw text labels
        font = pygame.font.SysFont(FONT_NAME, 24)
        
        # UI area label
        ui_label = font.render("UI AREA (No Grid)", True, (255, 255, 255))
        screen.blit(ui_label, (10, 10))
        
        # Game area label
        game_label = font.render(f"GAME AREA (Grid: {GRID_WIDTH}x{GRID_HEIGHT} cells)", True, (255, 255, 255))
        screen.blit(game_label, (10, GAME_AREA_TOP + 10))
        
        # Draw cell count info
        info_font = pygame.font.SysFont(FONT_NAME, 18)
        cell_info = f"Cell Size: {GRID_SIZE}px, Total Cells: {GRID_WIDTH * GRID_HEIGHT}"
        cell_surface = info_font.render(cell_info, True, (200, 200, 255))
        screen.blit(cell_surface, (10, GAME_AREA_TOP + 40))
        
        # Draw instructions
        instructions = "Press ESC to exit test"
        instr_surface = info_font.render(instructions, True, (200, 200, 200))
        screen.blit(instr_surface, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 30))
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    print("\nVisual test complete.")
    print("✓ Grid should only appear in game area (below red line)")
    print("✓ Snake and food will be confined to game area")
    print("✓ UI text remains visible above grid")

if __name__ == "__main__":
    test_grid_separation()