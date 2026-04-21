# Snake Game

A classic Snake game implementation using PyGame with professional code structure, modular design, and maintainable architecture.

## Features

- **Classic Snake Gameplay**: Move the snake, eat food, grow longer, avoid collisions
- **Score Tracking**: Real-time score display with high score persistence
- **Difficulty Levels**: Multiple speed settings (Easy, Medium, Hard)
- **Visual Polish**: Smooth animations, particle effects, and visual feedback
- **Sound Effects**: Immersive audio feedback for game events
- **Pause/Resume**: Game can be paused and resumed
- **Game Over Screen**: Clean game over screen with restart option
- **Configurable Settings**: Easy-to-modify game parameters

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
   python -m src.game
   ```

## Controls

- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **P**: Pause/Resume game
- **R**: Restart game (when game over)
- **ESC**: Quit game
- **1, 2, 3**: Change difficulty (Easy, Medium, Hard)

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Style
This project follows PEP 8 style guidelines. Use black for formatting:
```bash
black src/ tests/
```

### Adding New Features
1. Create a new module in `src/` for the feature
2. Add tests in `tests/`
3. Update configuration in `src/config.py` if needed
4. Document the feature in README.md

## Dependencies

- Python 3.8+
- PyGame 2.0+
- pytest (for testing)

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request