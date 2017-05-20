#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.

"""

# import the random and math library
import random
import math


def meImage():
    """
    Store my ascii image in a separat variabel as a raw string
    """
    return r"""
   www
  /n n\        /\
  |/^\|       /  \
  | , |       ^||^
   \_/         ||
   _U_         ||
 /`   `''-----'P3
/ |. .|''-----"||
\'|   |        ||
 \|   |        ||
  E   |        ||
 /#####\       ||
 /#####\       ||
   |||         ||
   |||         ||
   |||         ||
   |||         ||
  molom        Ll
    """

def menu():
    """
    Display the menu with the options that Marvin can do.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(meImage())
    print("Hi, I'm Emil. What's your name?")
    print("1) Present yourself to Emil.")
    print("2) Present your age to Emil.")
    print("3) Present your weight to Emil.")
    print("4) Convert minutes into hours.")
    print("5) Convert Celcius into Fahrenheit.")
    print("6) Word multiplikation.")
    print("7) Randomize a number.")
    print("8) Calculate the sum and the average.")
    print("9) Calculate your grade.")
    print("10) Calculate the area of a circle.")
    print("11) Calculate the hypotenuse of a right-angled triangle.")
    print("12) Compare numbers of your choice.")
    print("q) Quit.")


def myNameIs():
    """
    Read the users name and say hello to Marvin.
    """
    name = input("What is your name?\n--> ")
    print("Emil says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def myAgeIs():
    """
    Ask for the users name and print out a smartass answer
    """
    age = input("What is your age?\n--> ")

    # Make sure the user input is a valid number.
    if(age.isnumeric()):
        # Calculate the users age into seconds adding .24 to the number of
        # days to account for leap years.
        age = (((float(age) * 365.24) * float(24)) * float(60)) * float(60)

        # Print smartass answer.
        print("Emil says:\n")
        print("Hey, you have lived for %s seconds!" % age)
    else:
        print("You need to enter a valid number.")

def myMoonWeightIs():
    """
    Ask for the users weight and caculate his/her weight on the moon.
    """
    weight = input("What is your current weight?\n--> ")

    # Make sure the user input is a valid number.
    if(weight.isnumeric()):
        # Calculate the users weight on the moon.
        weight = float(weight) / 6.0

         # Print smartass answer.
        print("Emil says:\n")
        print("Your weight on the moon would be: " + str(round(weight, 2)))
    else:
        print("You must enter a valid number.")

def myMinutesToHours():
    """
    Convert the users input of minutes into hours.
    """
    userTime = input("How many minutes would you like to convert into hours?\n--> ")

    # Make sure the user input is a valid number.
    if(userTime.isnumeric()):
        userTime = int(userTime)
        hours = 0
        minutes = 0
        # If the amount of minutes entered contains at least 1 hour:
        if(userTime / 60 >= 1):
            # Turn the minutes into hours.
            hours = int(userTime / 60)

        # Remove the hours and get the minutes.
        minutes = userTime - (hours * 60)

        if(hours >= 1):
            print("That's: " + str(hours) + " hour(s) and " + str(minutes) + " minute(s).")
        elif(minutes > 0):
            print("That's " + str(minutes) + " minutes.")
        else:
            print("You must enter a value above 0.")
    else:
        print("You must enter a valid number.")

def celciusToFahren():
    """
    Request input from the user and turn Celcius into Fahrenheit.
    """
    celcius = input("Input temperature in Celcius to convert it.\n--> ")

    # Make sure the input is a number.
    if(celcius.isnumeric()):
        # Calculate Fahrenheit
        fahrenheit = round(float(celcius) * 9/5 + 32, 1)

        # Print the result.
        print(celcius + " Celcius is %s in Fahrenheit." % fahrenheit)
    else:
        print("Input must be a number.")

def wordMultiplikation():
    """
    Multiply a word by a user specific number of times.
    """
    word = input("Enter a ord: \n--> ")
    number = input("Enter a number: \n--> ")

    # Make sure the inputed number is numeric.
    if(number.isnumeric()):
        number = int(number)
        result = ""

        while(number > 0):
            result = result + " " + word
            number = number - 1

        print(result)

    else:
        print("Second input must be a number.")

def randomNumber():
    """
    Get the minimum and maximum value from the user, print 10 numbers in this range.
    """
    minNum = input("What is your minimum number?\n--> ")
    maxNum = input("What is your maximum number?\n--> ")

    # Make sure both input numbers are numeric.
    if(minNum.isnumeric() and maxNum.isnumeric()):
        iterator = 0
        result = ""

        # Randomize 10 numbers within the given range.
        while(iterator < 10):
            result = result + str(random.randrange(int(minNum), int(maxNum))) + ", "
            iterator = iterator + 1

        # Print the 10 randomized numbers.
        print(result)
    else:
        print("Both inputs must be numbers.")

def sunAndAvg():
    """
    Calculates the sum and the average of the user provided numbers.
    """
    result = ""
    nrOfNumbers = 0
    sumNum = 0.0
    loop = True

    # Ask the user for a number until the user types "done"
    while(loop):
        # Ask the user for a number.
        number = input("Enter a number or enter \"done\" to finish: \n--> ")

        # Make sure the input is numeric
        if(number.isnumeric()):
            result = result + number
            sumNum = sumNum + float(number)
            nrOfNumbers = nrOfNumbers + 1
        # Check if the input is "done"
        elif(number == "done"):
            loop = False
        # Warn the user that only numbers compute.
        else:
            print("WARNING! Input must be a number! Try again.")

    # Check if any numbers have been chosen. If not, do nothing.
    if(nrOfNumbers > 0):
        avg = sumNum / float(nrOfNumbers)

        print("The sum of your numbers is: %s." % sumNum)
        print("The average of your numbers is: %s." % avg)

def pointsToGrade():
    """
    Ask the user for max points and the users achieved points, print grade.
    """
    # Get input from the user.
    maxpoints = input("What is the maximum amount of points achievable on the test?\n--> ")
    userpoints = input("How many points did you get?\n--> ")

    # Make sure the input is numeric.
    if(maxpoints.isnumeric() and userpoints.isnumeric()):
        # Convert into correct values here to avoid unnecessary function calls.
        maxpoints = float(maxpoints)
        userpoints = int(maxpoints)

        # Check which grade the user has and print it.
        if(userpoints >= (maxpoints * 0.9)):
            print("Grade: A")
        elif(userpoints >= (maxpoints * 0.8)):
            print("Grade: B")
        elif(userpoints >= (maxpoints * 0.7)):
            print("Grade: C")
        elif(userpoints >= (maxpoints * 0.6)):
            print("Grade: D")
        elif(userpoints < (maxpoints * 0.6)):
            print("Grade: F")

    else:
        print("Both values must be numbers.")

def circleArea():
    """
    Calculate the area of a circle given a radian value.
    """
    radian = input("Enter a radian value:\n--> ")

    if(radian.isnumeric() and float(radian) > 0):
        area = math.pow(float(radian), 2) * math.pi

        print("The area of your circle is: %s" % area)
    else:
        print("The entered radian must be a valid non-negative number.")

def hypotenuse():
    """
    Calculate the hypotenuse of the users input.
    """
    # Get user input.
    side1 = input("Enter the first side/angle of the triangle:\n--> ")
    side2 = input("Enter the second side/angle of the triangle:\n--> ")

    if(side1.isnumeric() and side2.isnumeric() and side1 > 0 and side2 > 0):
        # Calculate the hypotenuse.
        hypoten = math.pow(side1, 2) + math.pow(side2, 2)

        print("The hypotenuse of your triangle is %s" % hypoten)
    else:
        print("The sides must be valid non-negative numbers.")

def myNumberComparison():
    """
    Compare the users number to the users previous number.
    """
    loop = True

    prevNum = input("Enter a number to compare to:\n--> ")

    if(prevNum.isnumeric()):
        prevNum = int(prevNum)
        while(loop):
            # Ask for a number to compare it with.
            newNum = input("Enter a number to compare it with or type \"done\" to exit.\n--> ")

            # Make sure the number is numeric and that the previous number is set.
            if(newNum.isnumeric()):
                newNum = int(newNum)
                # Make comparisons.
                if(prevNum < newNum):
                    print("The number {num1} is smaller than {num2}".format(num1=prevNum, num2=newNum))
                elif(prevNum > newNum):
                    print("The number {num1} is larger than {num2}".format(num1=prevNum, num2=newNum))
                elif(prevNum == newNum):
                    print("The number {num1} is the same as {num2}".format(num1=prevNum, num2=newNum))

                # Make the previous number our previous new number.
                prevNum = newNum

            elif(newNum == "done"):
                loop = False
            else:
                print("The entered value must be a number.")
    else:
        print("Input must be a number.")

def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call an appropriate
    function.
    """
    while True:
        menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            return

        elif choice == "1":
            myNameIs()

        elif choice == "2":
            myAgeIs()

        elif choice == "3":
            myMoonWeightIs()

        elif choice == "4":
            myMinutesToHours()

        elif choice == "5":
            celciusToFahren()

        elif choice == "6":
            wordMultiplikation()

        elif choice == "7":
            randomNumber()

        elif choice == "8":
            sunAndAvg()

        elif choice == "9":
            pointsToGrade()

        elif choice == "10":
            circleArea()

        elif choice == "11":
            hypotenuse()

        elif choice == "12":
            myNumberComparison()

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


# Check if the special name variable has the value "__main__"
# In order to determine if this file is being run as the source file "the main file"
if __name__ == "__main__":
    main()
