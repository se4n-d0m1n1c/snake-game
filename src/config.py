"""
Snake Game Configuration Module

This module contains all configuration constants and settings for the game.
Centralizing configuration makes the game easier to maintain and modify.
"""

import pygame

# ===== DISPLAY SETTINGS =====
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
UI_HEIGHT = 60  # Height of the UI bar at the top
GAME_AREA_TOP = UI_HEIGHT  # Where the game grid starts
GAME_AREA_HEIGHT = SCREEN_HEIGHT - UI_HEIGHT  # Height of playable area
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = GAME_AREA_HEIGHT // GRID_SIZE  # Grid height based on game area, not full screen

# ===== COLORS (RGB) =====
# Background colors
BACKGROUND_COLOR = (15, 15, 25)
GRID_COLOR = (30, 30, 40)

# Snake colors
SNAKE_HEAD_COLOR = (50, 205, 50)  # Lime green
SNAKE_BODY_COLOR = (34, 139, 34)  # Forest green
SNAKE_OUTLINE_COLOR = (0, 100, 0)  # Dark green

# Food colors
FOOD_COLOR = (220, 20, 60)  # Crimson red
FOOD_GLOW_COLOR = (255, 100, 100)  # Light red

# UI colors
UI_BACKGROUND = (20, 20, 30, 200)  # Semi-transparent dark
UI_TEXT_COLOR = (240, 240, 240)
UI_ACCENT_COLOR = (70, 130, 180)  # Steel blue
UI_WARNING_COLOR = (255, 215, 0)  # Gold

# ===== GAME SETTINGS =====
# Difficulty levels (frames per move - higher is slower/easier, lower is faster/harder)
DIFFICULTY_SPEEDS = {
    "easy": 20,    # Slow - easier (20 frames between moves)
    "medium": 15,  # Normal (15 frames between moves)
    "hard": 10,    # Fast - harder (10 frames between moves)
}

INITIAL_SPEED = DIFFICULTY_SPEEDS["medium"]
INITIAL_SNAKE_LENGTH = 3
FOOD_SCORE_VALUE = 10
HIGH_SCORE_FILE = "highscore.txt"

# ===== FONT SETTINGS =====
FONT_NAME = "Arial"
FONT_SIZES = {
    "title": 48,
    "heading": 36,
    "normal": 24,
    "small": 18,
}

# ===== SOUND SETTINGS =====
SOUND_ENABLED = True
SOUND_VOLUME = 0.5

# ===== ANIMATION SETTINGS =====
ANIMATION_FPS = 60
PARTICLE_LIFETIME = 30  # frames

# ===== KEY BINDINGS =====
KEY_UP = pygame.K_UP
KEY_DOWN = pygame.K_DOWN
KEY_LEFT = pygame.K_LEFT
KEY_RIGHT = pygame.K_RIGHT
KEY_PAUSE = pygame.K_p
KEY_RESTART = pygame.K_r
KEY_QUIT = pygame.K_ESCAPE
KEY_EASY = pygame.K_1
KEY_MEDIUM = pygame.K_2
KEY_HARD = pygame.K_3

# ===== GAME STATES =====
STATE_MENU = "menu"
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_GAME_OVER = "game_over"

# ===== DIRECTION VECTORS =====
DIRECTION_UP = (0, -1)
DIRECTION_DOWN = (0, 1)
DIRECTION_LEFT = (-1, 0)
DIRECTION_RIGHT = (1, 0)