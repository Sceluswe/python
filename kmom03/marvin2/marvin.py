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
import datetime

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
    print("Hi, I'm Marvin. What's your name?")
    print("1) Present yourself to Marvin.")
    print("2) Present your age to Marvin.")
    print("3) Present your weight to Marvin.")
    print("4) Convert minutes into hours.")
    print("5) Convert Celcius into Fahrenheit.")
    print("6) Word multiplikation.")
    print("7) Randomize a number.")
    print("8) Calculate the sum and the average.")
    print("9) Calculate your grade.")
    print("10) Calculate the area of a circle.")
    print("11) Calculate the hypotenuse of a right-angled triangle.")
    print("12) Compare numbers of your choice.")
    print("13) Play the game: \"Guess the Number\".")
    print("14) Display some info about me (Marvin).")
    print("15) Shuffle a word.")
    print("16) Play the game: \"Guess the Word\".")
    print("q) Quit.")


def myNameIs():
    """
    Read the users name and say hello to Marvin.
    """
    name = input("What is your name?\n--> ")
    print("Marvin says:\n")
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
        print("Marvin says:\n")
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
        print("Marvin says:\n")
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

def sumAndAvg():
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
            # Calculate the result.
            result = result + number
            # Calculate the sum of all numbers.
            sumNum = sumNum + float(number)
            # Calculate how many numbers the user entered.
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

"""
Kmom03:

"""

def myGuessTheNumber():
    """
    Randomize a number and let the user guess which number it is.
    """

    # Randomize a number.
    marvinsNum = random.randrange(1, 100)

    # Ask the player for his guesses until the player quits or wins.
    loop = True
    nrOfGuesses = 6

    while(loop):
        # If the player runs out of guesses ask him if he wants to play again or not.
        if(nrOfGuesses == 0):
            userGuess = input("You've run out of guesses. Type \"p\" to play again or \"q\" to quit\n--> ")
        else:
            userGuess = input("Try to guess my number! It's between 1-100, or type \"q\" to quit.\n--> ")

        # Make sure the players guess is a number.
        if(userGuess.isnumeric()):
            # Check if the player has won.
            if(int(userGuess) == marvinsNum):
                print("Congratulations you guessed the right number: " + str(marvinsNum))
                print("Type \"p\" to play again, or \"q\" to quit.")
            elif(int(userGuess) > marvinsNum):
                print("That's too high! You have " + str(nrOfGuesses - 1) + " guesses left.")
                nrOfGuesses = nrOfGuesses - 1
            elif(int(userGuess) < marvinsNum):
                print("That's too small! You have " + str(nrOfGuesses - 1) + " guesses left.")
                nrOfGuesses = nrOfGuesses - 1

        elif(userGuess == "p"):
            marvinsNum = random.randrange(1, 100)
            nrOfGuesses = 6

        elif(userGuess == "q"):
            print("Thank you for playing!")
            loop = False

        else:
            print("Your guess must be a number. Try again.")

def marvinInfo():
    """
    A function that prints some information about marvin
    and the durrent day.
    """

    myFile = open("marvinInfo.txt", "r")
    marvinSays = myFile.read()
    myFile.close()

    # Get our date and time.
    mDate = str(datetime.datetime.now())
    mTime = mDate[11:-10]
    mDate = mDate[:10]

    # Randomize marvins mood.
    mMood = ""
    ranNumb = random.randrange(1, 3)
    if(ranNumb == 1):
        mMood = "exalted"
    elif(ranNumb == 2):
        mMood = "morrows"
    elif(mMood == 3):
        mMood = "excited"

    # Randomize an age for marvin.
    mAge = random.randrange(1, 1000)

    # Remember to round this off to 3 decimals. I don't
    # remember the function name.
    mSize = round(float(mAge) / 33.33, 2)

    # Format the string and print the result.
    print(marvinSays.format(date=mDate, time=mTime, mood=mMood, age=mAge, size=mSize))

def shuffleMyWord():
    """
    Ask the user for a string, shuffle it and print it.
    """
    myString = input("Enter a word you'd like to shuffle.\n--> ")

    shuffled = list(myString)
    random.shuffle(shuffled)
    resString = ''.join(shuffled)

    print("Here's the shuffle: " + resString)

def myGuessTheWord():
    """
    Shuffle a word and let the user guess what word it is.
    """
    # Open the file and get all words in a list.
    myFile = open("guessTheWord.txt", "r")
    myLinesList = myFile.readlines()
    myFile.close()

    # Randomize a number
    randNum = random.randrange(0, len(myLinesList))
    # Use the random number to randomly pick a line in the file.
    # And strip it off the newline tag \n
    myLine = myLinesList[randNum].strip() # does this really return a string?
    # Turn the string into a list.
    myWord = list(myLine)
    # Save the answer.
    theAnswer = ''.join(myWord)
    # Shuffle.
    random.shuffle(myWord)
    # Turn the list into a string.
    myShuffledWord = ''.join(myWord)

    # Ask the viewer for his guess until he is correct or types "q".
    loop = True

    while(loop):
        uGuess = input("Can you guess what word this is:\n" + myShuffledWord + "\nor type \"q\" to quit.\n--> ")

        # Make sure the input is alphabetic.
        if(uGuess.isnumeric() is False):
            if(uGuess == theAnswer):
                print("You guessed it! Winner!")
                loop = False

            elif(uGuess == "q"):
                print("Goodbye!")
                loop = False

            else:
                print("Try again!")
        else:
            print("The entered number must be alphabetic!")
