# Tic-Tac-Toe Game

This project is a simple implementation of the classic Tic-Tac-Toe game using Python and Pygame. Players take turns clicking on the grid to place their marks (“X” or “O”), and the game detects a winner or resets for a new game.

## Features
- A 3x3 grid for gameplay.
- Interactive player turns: Player 1 (“O”) and Player 2 (“X”).
- Automatically detects winning conditions.
- Option to restart the game by pressing the `SPACE` key.
- Visual representation using Pygame for icons and the grid.

## Requirements
To run this project, ensure you have the following installed:

- Python 3.x
- Pygame library

Install Pygame using:
```bash
pip install pygame
```

## How to Run
1. Clone this repository or download the source code.
2. Place the required icon images (`x.png`, `o.png`, `grid.png`) in the `icons` folder at the same level as the script.
3. Run the script using:
```bash
python <script_name>.py
```
4. Click on the grid to play the game. Player 1 starts as “O” and Player 2 follows as “X”.
5. To reset the game, press the `SPACE` key.

## File Structure
```
.
|-- script_name.py   # The main Python script
|-- icons            # Folder containing icon images
    |-- x.png        # Icon for Player X
    |-- o.png        # Icon for Player O
    |-- grid.png     # Grid image for the board
```

## Game Logic
### How It Works:
1. **Grid Layout**: The board is divided into a 3x3 grid where each cell’s position is calculated based on the mouse click.
2. **Player Turns**: Alternates between Player 1 (“O”) and Player 2 (“X”).
3. **Winner Detection**:
   - Rows: Checks if all cells in a row have the same mark.
   - Columns: Checks if all cells in a column have the same mark.
   - Diagonals: Checks both diagonals for matching marks.
4. **Reset**: Pressing the `SPACE` key clears the board for a new game.

### Winning Condition
When a player places three of their marks in a row, column, or diagonal, a message appears on the screen, and the game resets after 2 seconds.

## Screenshots

### Initial Grid
![](./screenshots/initial_grid.png)

### Gameplay
![](./screenshots/gameplay.png)

### Winning Message
![](./screenshots/winning_message.png)

## Future Improvements
- Add an AI opponent for single-player mode.
- Enhance visuals and animations.
- Implement a score-tracking system.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Enjoy playing Tic-Tac-Toe!

