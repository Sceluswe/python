#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module asks the user for input and displays an item in return.
This main function functions as a menu.
"""

# Import marvin.
import marvin

def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call an appropriate
    function.
    """
    while True:
        marvin.menu()
        choice = input("--> ")

        # Turn choice into all lowercase.
        choice = choice.lower()

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            return

        elif choice == "1":
            marvin.myNameIs()

        elif choice == "2":
            marvin.myAgeIs()

        elif choice == "3":
            marvin.myMoonWeightIs()

        elif choice == "4":
            marvin.myMinutesToHours()

        elif choice == "5":
            marvin.celciusToFahren()

        elif choice == "6":
            marvin.wordMultiplikation()

        elif choice == "7":
            marvin.randomNumber()

        elif choice == "8":
            marvin.sumAndAvg()

        elif choice == "9":
            marvin.pointsToGrade()

        elif choice == "10":
            marvin.circleArea()

        elif choice == "11":
            marvin.hypotenuse()

        elif choice == "12":
            marvin.myNumberComparison()

        elif choice == "13":
            marvin.myGuessTheNumber()

        elif choice == "14":
            marvin.marvinInfo()

        elif choice == "15":
            marvin.shuffleMyWord()

        elif choice == "16":
            marvin.myGuessTheWord()

        elif choice == "17":
            marvin.analyzeTextfile()

        elif "citat" in choice:
            marvin.getQuoteResponse()

        elif "hej" in choice:
            marvin.getGreetingResponse()

        elif "lunch" in choice:
            marvin.getLunchResponse()

        elif "inv pick" in choice and len(choice) > 9:
            marvin.pickItem(choice[9:])

        elif "inv drop" in choice and len(choice) > 9:
            marvin.dropItem(choice[9:])

        elif "inv drop" in choice:
            marvin.dropEntireInventory()

        elif "inv" in choice:
            marvin.getInventory()

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


# Check if the special name variable has the value "__main__"
# In order to determine if this file is being run as the source file "the main file"
if __name__ == "__main__":
    main()
