"""
Audio Manager Module

This module handles sound effects and music for the game.
Includes fallback for systems without audio support.
"""

import pygame
import os
from typing import Optional
from config import *


class AudioManager:
    """Manages game audio including sound effects and music."""
    
    def __init__(self):
        """Initialize the audio manager."""
        self.sounds = {}
        self.music_playing = False
        self.enabled = SOUND_ENABLED
        
        # Initialize PyGame mixer if audio is enabled
        if self.enabled:
            try:
                pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
                self._load_sounds()
            except:
                self.enabled = False
                print("Audio initialization failed. Continuing without sound.")
    
    def _load_sounds(self) -> None:
        """Load or generate sound effects."""
        if not self.enabled:
            return
            
        # Generate simple sound effects programmatically
        self._generate_sounds()
    
    def _generate_sounds(self) -> None:
        """Generate basic sound effects using PyGame."""
        try:
            # Eat sound (short beep)
            eat_sound = pygame.mixer.Sound(buffer=bytes([128] * 1000))
            eat_sound.set_volume(0.3)
            self.sounds["eat"] = eat_sound
            
            # Game over sound (lower pitch)
            game_over_sound = pygame.mixer.Sound(buffer=bytes([64] * 2000))
            game_over_sound.set_volume(0.4)
            self.sounds["game_over"] = game_over_sound
            
            # Move sound (very short click)
            move_sound = pygame.mixer.Sound(buffer=bytes([200] * 500))
            move_sound.set_volume(0.1)
            self.sounds["move"] = move_sound
            
        except:
            # If sound generation fails, disable audio
            self.enabled = False
    
    def play_sound(self, sound_name: str) -> None:
        """
        Play a sound effect.
        
        Args:
            sound_name: Name of the sound to play.
        """
        if self.enabled and sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
            except:
                pass  # Silently fail if sound playback fails
    
    def play_eat_sound(self) -> None:
        """Play the sound for eating food."""
        self.play_sound("eat")
    
    def play_game_over_sound(self) -> None:
        """Play the game over sound."""
        self.play_sound("game_over")
    
    def play_move_sound(self) -> None:
        """Play the movement sound."""
        self.play_sound("move")
    
    def play_background_music(self) -> None:
        """Play background music (if available)."""
        if self.enabled and not self.music_playing:
            try:
                # Try to load music file if it exists
                music_path = os.path.join("assets", "sounds", "background.ogg")
                if os.path.exists(music_path):
                    pygame.mixer.music.load(music_path)
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(-1)  # Loop indefinitely
                    self.music_playing = True
            except:
                pass
    
    def stop_background_music(self) -> None:
        """Stop background music."""
        if self.enabled and self.music_playing:
            try:
                pygame.mixer.music.stop()
                self.music_playing = False
            except:
                pass
    
    def pause_background_music(self) -> None:
        """Pause background music."""
        if self.enabled and self.music_playing:
            try:
                pygame.mixer.music.pause()
            except:
                pass
    
    def resume_background_music(self) -> None:
        """Resume background music."""
        if self.enabled and self.music_playing:
            try:
                pygame.mixer.music.unpause()
            except:
                pass
    
    def set_volume(self, volume: float) -> None:
        """
        Set the master volume.
        
        Args:
            volume: Volume level (0.0 to 1.0).
        """
        if self.enabled:
            try:
                pygame.mixer.music.set_volume(volume)
                for sound in self.sounds.values():
                    sound.set_volume(volume)
            except:
                pass
    
    def cleanup(self) -> None:
        """Clean up audio resources."""
        if self.enabled:
            try:
                self.stop_background_music()
                pygame.mixer.quit()
            except:
                pass