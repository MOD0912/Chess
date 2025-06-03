# Chess Game

This project is a simple implementation of a chess game using Python and the Ursina game engine. It provides a graphical interface for playing chess against another player.

## Project Structure

- **main.py**: Contains the main logic for the chess game, including the initialization of the game board and pieces, as well as handling user input.
- **piece.py**: Defines the `Piece` class, which represents individual chess pieces and their properties such as texture, position, color, and scale.
- **assets/textures**: Directory containing image files for the chess pieces, including textures for both black and white pieces.
- **TODO.md**: A file for tracking tasks and features that need to be implemented or improved in the project.
- **.gitignore**: Specifies files and directories that should be ignored by Git, such as temporary files and compiled files.
- **README.md**: This file, providing an overview of the project, how to run it, and controls.
- **LICENSE**: The license file for the project, specifying the terms under which the code can be used and modified.
- **requirements.txt**: Lists the dependencies required to run the project. At this time, the only required dependency is the Ursina game engine.

## How to Run the Game

1. Ensure you have Python installed on your machine.
2. Install the Ursina game engine if you haven't already:
   ```
   pip install ursina
   ```
3. Run the game by executing the following command in your terminal:
   ```
   python main.py
   ```

## Controls

- Use the mouse to select and move pieces on the board.
- Press "Control" to exit the game.

## Future Improvements

- Implement AI for single-player mode.
- Add a timer for each player.
- Enhance the user interface with additional features.

Feel free to contribute to the project by adding new features or improving existing ones!