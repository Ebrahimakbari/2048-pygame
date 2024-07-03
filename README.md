# 2048 pygame

This code is a Python implementation of the popular 2048 game. The game is played on a 4x4 grid, and the goal is to combine numbered tiles to create a tile with the number 2048. The code includes classes for tiles, functions for moving and merging tiles, generating new tiles, and updating the game display.

## Tile Class

The `Tile` class represents a single tile in the game. It has properties for its value, row, and column, as well as methods for drawing itself, setting its position, and moving.

## end_move Function

The `end_move` function checks if the game is over by seeing if there are 16 tiles on the board. If there are, it returns "lost". Otherwise, it adds a new tile to a random position and returns "continue".

## update_tiles Function

The `update_tiles` function sorts the tiles by their column and then by their row, and updates the tile positions accordingly.

## move_tiles Function

The `move_tiles` function handles the movement of the tiles based on the given direction. It checks for boundary conditions, merges tiles if they have the same value, and moves tiles accordingly.

## get_random_pos Function

The `get_random_pos` function generates a random position on the grid that is not already occupied by a tile.

## generate_tiles Function

The `generate_tiles` function creates a new set of tiles with two tiles initialized to 2.

## draw_grid Function

The `draw_grid` function draws the grid lines on the window.

## draw Function

The `draw` function fills the window with the background color, draws the tiles, and then draws the grid lines.

## main Function

The `main` function sets up the game window, initializes the tiles, and runs the game loop. It listens for key events to move the tiles and updates the display accordingly. If the game is over, it prints "Game Over" and exits.

To run the game, simply copy and paste the code into a Python environment and execute it. The game window will appear, and you can use the arrow keys to move the tiles.
