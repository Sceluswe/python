#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A text based viking adventure game, with puzzels.
"""
import os
import sys
import getopt
import game
import border

#from bs4 import UnicodeDammit

#
# Add some stuff about this script
#
PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Emil Mattsson"
EMAIL = "emilcbm@gmail.com"
VERSION = "1.0.0"
USAGE = """{program} - Print my name. By {author} ({email}), version {version}.
Usage:
  {program} [options] command [arguments-to-the-command]
Options:
  -h --help                      Display this help message.
  -i --info                      Print the game concept.
  -v --version                   Print version and exit.
  -a --about                     Print description about the creator.
  -c --cheat                     Tells you how to cheat through the game.

""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)

INFO = "Ett textbaserat äventyrsspel med pussel."

ABOUTME = """{author} är student på Bleking Tekniska högskola""".format(author=AUTHOR)
ABOUTME += "och en ödmjuk novis till den allsmäktige Mos."
ABOUTME += " För att utveckla sin filosofiska kodknackningsförmåga kämpar "
ABOUTME += "han emot legionnerna av prokrastinering och okunskap."

CHEAT = "Ladda filen med kommandot: \"load fusk\", skriv \"a yxa\" och sen fram. Tryck \"q\" i labyrinten."

MSG_VERSION = "{program} version {version}.".format(program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)

# Exit status 0
EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2



def parseOptions():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """
    # Switch through all options
    try:
        # Get the arguments from the command-line.
        # arg1 is the argument list to be parsed.
        # arg2 is the short name for the options ":" indicates the option
        # needs an argument.
        # arg3 is the long name version of each option.
        longopts_arr = ["help", "info", "version", "about", "cheat"]
        opts, args = getopt.getopt(sys.argv[1:], "hivac", longopts_arr)

        # Check which one of the options has been selected.
        for opt, arg in opts:
            # Print the help options and exit with status code 0.
            # -------- Standard options --------
            if opt in ("-h", "--help"):
                print(USAGE)
            elif opt in ("-i", "--info"):
                print(INFO)
            elif opt in ("-v", "--version"):
                print(VERSION)
            elif opt in ("-a", "--about"):
                print(ABOUTME)
            elif opt in ("-c", "--cheat"):
                print(CHEAT)
            else:
                assert False, "Unhandled option" + arg

        if len(args) >= 1:
            print("This module does not handle arguments.")

    except Exception as err:
        print(err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        #traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)



def main():
    """
    Main function to carry out the work.
    """
    # Handle the arguments.
    parseOptions()

    introtext = "\nSom viking har du plundrat kusterna i hertig Mos land."

    introtext += " Nu har han fått tag på dig och kastat ned dig och din trogne tjänare Marvin, i ett fängelse."

    introtext += " Fängelset består av sju rum, sju tester. Mos gjorde det klart för dig att om du klarar alla testerna"

    introtext += " så kan du vinna din frihet. Marvin, ständigt trogen, erbjuder sig att följa dina befallningar."

    introtext += " Börja med att be honom om hjälp."

    print("\n" + introtext + "\n")

    # Load rooms from JSON file.
    game.loadDefaultGame("rooms.txt", "inv.txt")
    print("\n" + game.getRoomDescription() + "\n")

    while True:
        # get user input.
        choice = input("--> ")
        if choice == "quit":
            break

        # Parse commands.
        game.commandMenu(choice)

        if game.ACTIVEROOM == "room7":
            break

    if game.ACTIVEROOM == "room7":
        border.main()

        print("\nSeger! Friheten är återfådd.\n")

    #input("\nÖka storleken för att se fångens ansikte, tryck sedan enter... \n")


    sys.exit(EXIT_SUCCESS)

if __name__ == "__main__":
    main()
