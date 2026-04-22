# Snake Game

A classic Snake game implementation using PyGame.

## Features

- **Classic Snake Gameplay**: Move the snake, eat food, grow longer, avoid collisions
- **Score Tracking**: Real-time score display with high score persistence
- **Difficulty Levels**: Multiple speed settings (Easy, Medium, Hard)
- **Visual Polish**: Smooth animations, particle effects, and visual feedback
- **Sound Effects**: Immersive audio feedback for game events
- **Pause/Resume**: Game can be paused and resumed
- **Game Over Screen**: Clean game over screen with restart option
- **Two-Step Menu**: Main menu with play button → Difficulty selection before gameplay

## Project Structure

```
snake-game/
├── src/
│   ├── __init__.py
│   ├── game.py          # Main game loop and state management
│   ├── snake.py         # Snake class with movement logic
│   ├── food.py          # Food generation and collision
│   ├── ui.py            # User interface rendering
│   ├── audio.py         # Sound effects and music management
│   └── config.py        # Game configuration and constants
├── assets/
│   ├── fonts/           # Font files
│   ├── sounds/          # Sound effects
│   └── images/          # Game graphics (optional)
├── tests/
│   ├── test_snake.py
│   └── test_food.py
├── run.py            # Game entry point
├── requirements.txt     # Python dependencies
├── setup.py            # Package installation
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # This file
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/se4n-d0m1n1c/snake-game.git
   cd snake-game
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python run.py
   ```

## Controls

### Main Menu
- **ENTER/SPACE**: Proceed to difficulty selection
- **ESC**: Quit game

### Difficulty Selection
- **1**: Select Easy difficulty and start game
- **2**: Select Medium difficulty and start game  
- **3**: Select Hard difficulty and start game
- **ESC**: Go back to main menu

### Gameplay
- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **P**: Pause/Resume game
- **R**: Return to main menu
- **ESC**: Return to main menu

## Development

This project uses a modular structure with separate files for game logic, UI, audio, and configuration. The code is organized to be easy to understand and modify.

## Dependencies

- Python 3.8+
- PyGame 2.0+
- pytest (for testing)

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.