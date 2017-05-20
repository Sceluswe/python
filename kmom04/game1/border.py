#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testing out the curses lib.
"""

import curses


def main(scr):
    """
    Draw a border around the screen, move around using the cursor and leave a
    mark of the latest pressed character on the keyboard.

    Perhaps you could make a nice painting using asciart?

    Quit using 'q'.
    """

    # Clear the screen of any output
    scr.clear()

    # Get screen dimensions
    y1, x1 = scr.getmaxyx()
    # Why minus 1?
    # Minus 1 because otherwise a character can be written in the
    # bottom lower corner, which somehow breaks the game.
    y1 -= 1
    x1 -= 1

    y0, x0 = 0, 0

    # Get center position
    yc, xc = (y1-y0)//2, (x1-x0)//2

    # Create 2D array for the gameworld.
    gameWorld = []
    for y in range(y1):
        gameWorld.append([])
        for x in range(x1):
            gameWorld[y].append(" ")

    # Draw a border
    scr.border()

    # Move cursor to center
    scr.move(yc, xc)

    # Refresh to draw out
    scr.refresh()

    # Main loop
    x = xc
    y = yc
    ch = 'o'

    while True:
        key = scr.getkey()
        if key == 'q':
            break
        elif key == 's':
            # Open file and write each "gameworld" line to file.
            # e == empty.
            with open("border.txt", "w") as saveFile:
                for ys in range(y1):
                    row = ""
                    for xs in range(x1):
                        row += gameWorld[ys][xs]
                    saveFile.write(row + "\n")
        elif key == 'o':
            # Open the file and read a saved world from it.
            with open("border.txt", "r") as loadFile:
                # Get all lines from the file.
                tempStr = loadFile.read()
                # Find the amount of x's. Minus one to remove the line ending.
                # X is equal to the characters on a line.
                x_size = int(tempStr.find("\n"))
                # Find out the amount of y's.
                # Y is equal to the amount of lines.
                y_size = tempStr.count("\n")
                # Set the new max x and y.
                y1 = y_size if y1 >= y_size else y1
                x1 = x_size if x1 >= x_size else x1
                # Remove newline characters.
                tempStr = tempStr.replace("\n", "")
                # Split the string into a list.
                temp_list = list(tempStr)
                # Recreate the gameWorld array.
                gameWorld = []
                for yi in range(y1):
                    gameWorld.append([])
                # Write each character into our game array and into the window.
                for yi in range(y1):
                    for xi in range(x1):
                        gameWorld[yi].append(temp_list[xi + (yi * x1)])
                        # Write it into the window.
                        scr.addstr(yi, xi, gameWorld[yi][xi])
                # Calculate new center.
                yc, xc = (y1-y0)//2, (x1-x0)//2
                x = xc
                y = yc
                scr.move(yc, xc)
        elif key == 'KEY_UP':
            if y - 1 >= 0:
                y -= 1
        elif key == 'KEY_DOWN':
            if y + 1 <= y1 - 1:
                y += 1
        elif key == 'KEY_LEFT':
            if x - 1 >= 0:
                x -= 1
        elif key == 'KEY_RIGHT':
            if x + 1 <= x1 - 1:
                x += 1
        else:
            ch = key

        # Draw out the char at cursor position
        scr.addstr(ch)

        # Move cursor to new position
        scr.move(y, x)

        # Add the character to the gameWorld array.
        gameWorld[y][x] = ch

        # Redraw all items on the screen
        scr.refresh()


if __name__ == "__main__":
    print(__doc__)
    print(main.__doc__)
    input("Press enter to begin playing...")
    curses.wrapper(main)
