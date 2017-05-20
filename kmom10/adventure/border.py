#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Det sista testet.
"""

import curses



def saveGame(y1, x1, gameWorld):
    """
    Save the game state to file.
    """
    # Open file and write each "gameworld" line to file.
    # e == empty.
    with open("border.txt", "w") as saveFile:
        for ys in range(y1):
            row = ""
            for xs in range(x1):
                row += gameWorld[ys][xs]
            saveFile.write(row + "\n")



def loadGame(theFile):
    """
    Load a map from file.
    """
    # Open the file and read a saved world from it.
    tempStr = ""
    with open(theFile, "r") as loadFile:
        # Get all lines from the file.
        tempStr = loadFile.read()

    # Find the amount of x's. Minus one to remove the line ending.
    # X is equal to the characters on a line.
    x_size = int(tempStr.find("\n"))
    # Find out the amount of y's.
    # Y is equal to the amount of lines.
    y_size = tempStr.count("\n")
    # Remove newline characters.
    tempStr = tempStr.replace("\n", "")
    # return list of values.
    return [y_size, x_size, list(tempStr)]



def allocateGameWorld(y1, x1, arg_list):
    """
    Create the gameworld with the provided list and size values.
    """
    # Recreate the gameWorld array.
    gameWorld = []
    for yi in range(y1):
        gameWorld.append([])
    # Write each character into our game array and into the window.
    for yi in range(y1):
        for xi in range(x1):
            gameWorld[yi].append(arg_list[xi + (yi * x1)])

    # Return the new gameWorld array.
    return gameWorld



def main(scr=""):
    """
    Launches the game.
    """
    print("\nDu kan spara din framfart genom att trycka 's' när du vill och du kan ladda med 'o'.\n")
    print("\nNär du klarat labyrint testet så är du fri Hertig Mos grepp. Hitta nyckeln: K och vägen ut: E.\n")

    input("\nTryck enter för att gå in i labyrinten...\n")

    unlocked = False

    y0, x0 = 0, 0

    # load the proper file:
    temp_list = loadGame("defaultMaze.txt")

    #set y1 and x1 to new values.
    y1 = temp_list[0]
    x1 = temp_list[1]

    # Get the new world list.
    gameWorld = allocateGameWorld(y1, x1, temp_list[2])

    # Get center position
    yc, xc = (y1-y0)//2, (x1-x0)//2
    x = xc
    y = yc
    #scr = curses.newwin(y1, x1, x, y)
    # Initiate curses app.
    scr = curses.initscr()
    # Make sure it doesn't echo.
    curses.noecho()
    # Run cbreak mode to remove enter button requirement.
    curses.cbreak()
    # Enable special value keys like arrows.
    scr.keypad(True)
    # Clear the screen of any output
    scr.clear()
    # Write it into the window.
    for yi in range(y1):
        for xi in range(x1):
            scr.addstr(yi, xi, gameWorld[yi][xi])
    # Draw a border
    scr.border()
    # Move cursor to center
    scr.move(yc, xc)
    # Refresh to draw out
    scr.refresh()
    # Main loop
    ch = 'o'
    gameLoop = True

    while gameLoop:
        key = scr.getkey()
        if key == 'q':
            break

        elif key == 's':
            saveGame(y1, x1, gameWorld)

        elif key == 'o':
            # load the proper file:
            temp_list = loadGame("border.txt")

            #set y1 and x1 to new values.
            y1 = temp_list[0]
            x1 = temp_list[1]

            # Get the new world list.
            gameWorld = allocateGameWorld(y1, x1, temp_list[2])
            # Write it into the window.
            for yi in range(y1):
                for xi in range(x1):
                    scr.addstr(yi, xi, gameWorld[yi][xi])
            # Calculate new center.
            yc, xc = (y1-y0)//2, (x1-x0)//2
            x = xc
            y = yc
            scr.move(yc, xc)

        elif key == 'KEY_UP':
            if gameWorld[y - 1][x] == "E" and unlocked is True:
                if y - 1 >= 0:
                    y -= 1
            elif gameWorld[y - 1][x] == " " or gameWorld[y - 1][x] == "K":
                if y - 1 >= 0:
                    y -= 1

        elif key == 'KEY_DOWN':
            if gameWorld[y + 1][x] == "E" and unlocked is True:
                if y + 1 <= y1 - 1:
                    y += 1
            elif gameWorld[y + 1][x] == " " or gameWorld[y + 1][x] == "K":
                if y + 1 <= y1 - 1:
                    y += 1

        elif key == 'KEY_LEFT':
            if gameWorld[y][x - 1] == "E" and unlocked is True:
                if x - 1 >= 0:
                    x -= 1
            elif gameWorld[y][x - 1] == " " or gameWorld[y][x - 1] == "K":
                if x - 1 >= 0:
                    x -= 1

        elif key == 'KEY_RIGHT':
            if gameWorld[y][x + 1] == "E" and unlocked is True:
                if x + 1 <= x1 - 1:
                    x += 1
            if gameWorld[y][x + 1] == " " or gameWorld[y][x + 1] == "K":
                if x + 1 <= x1 - 1:
                    x += 1
        else:
            ch = key

        if gameWorld[y][x] == "K":
            unlocked = True
            gameWorld[y][x] = " "

        if gameWorld[y][x] == "E":
            if unlocked:
                gameLoop = False
                break

        if gameWorld[y][x] == " ":
            # Move cursor to new position
            scr.move(y, x)

            # Draw out the char at cursor position
            scr.addstr(ch)

        # Redraw all items on the screen
        scr.refresh()

    curses.nocbreak()
    scr.keypad(False)
    curses.echo()
    curses.endwin()


if __name__ == "__main__":
    print(__doc__)
    print(main.__doc__)
    input("Press enter to begin playing...")
    curses.wrapper(main)
