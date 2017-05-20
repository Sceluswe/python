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
import json
import re

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
    print("17) Analyze textfile")
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
    # And strip it of the newline tag \n
    myLine = myLinesList[randNum].strip()

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
        if(uGuess.isnumeric() is not False):
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

def getQuoteResponse():
    """
    Get a quote from marvin, in response to the word "citat".
    """
    # Open the file with the quotes.
    quoteFile = open("quotes.txt", "r")
    # Get all lines into a list and remove line endings.
    allQuotes = quoteFile.read().split('\n')
    # Close the file.
    quoteFile.close()
    # Get a random number used to select a quote.
    randNum = random.randrange(0, len(allQuotes))
    print("\n" + allQuotes[randNum] + "\n")


def getGreetingResponse():
    """
    Get a gretting from marvin in response to a users greeting.
    """
    hello = ['Hej själv! ', 'Trevligt att du bryr dig om mig. ',
             'Det var länge sedan någon var trevlig mot mig. ',
             'Halloj, det ser ut att bli mulet idag. ',]

    msgs = ['Ja, vad kan jag göra för Dig?',
            'Låt mig hjälpa dig med dina strävanden.',
            'Ursäkta, vad önskas?',
            'Kan jag stå till din tjänst?',
            'Jag kan svara på alla dina frågor.',
            'Ge me hög-fem!',
            'Jag svarar endast inför mos, det är min enda herre.',
            'mos är kungen!',
            'Oh, ursäkta, jag slumrade visst till.',
            'Fråga, länka till exempel samt source.php/gist/codeshare och vänta på svaret.']

    smile = [':-D', ':-P', ';-P', ';-)', ':-)', '8-)']

    # Add the two lists together.
    tempList = hello + msgs + smile
    # Randomize a standard response to "hej"
    randNum = random.randrange(0, len(tempList))
    print("\n" + tempList[randNum] + "\n")


def getLunchResponse():
    """
    Get a lunch suggestion from marvin.
    """
    lunchQuote = ['ska vi ta %s?',
                  'ska vi dra ned till %s?',
                  'jag tänkte käka på %s, ska du med?',
                  'På %s är det mysigt, ska vi ta där?']

    lunchStan = ['Olles krovbar',
                 'Lila thai stället',
                 'donken',
                 'tex mex stället vid subway',
                 'Subway',
                 'Nya peking',
                 'kebab house',
                 'Royal thai',
                 'thai stället vid hemmakväll',
                 'Gelato',
                 'Indian garden',
                 'Sumo sushi',
                 'Pasterian i stan',
                 'Biobaren',
                 'Michelangelo']

    # Randomize a standard phrase.
    randLunchQuote = random.randrange(0, len(lunchQuote))
    # Randomize a place to eat.
    randPlace = random.randrange(0, len(lunchStan))
    # Add them together and print.
    print("\n" + lunchQuote[randLunchQuote] % lunchStan[randPlace] + "\n")

"""

Kmom04:

"""

def loadInventory():
    """
    Loads the inventory and puts it in a list.
    Returns the list.
    """
    inventory = []
    with open("inv.data", "r") as inventory_file:
        inventory = inventory_file.readlines()

    return inventory

def loadJSONInventory():
    """
    Load the inventory from a JSON file.
    Return the items as a list.
    """
    # Create the list to return.
    inventory = []
    # Try to create the file, if it exists just move on.
    try:
        with open('json.txt', "x") as JSONfile:
            JSONfile.write("{\n    \"marvinArray\": [\n\n    ]\n}")
    except FileExistsError:
        pass
    # Load the JSON file.
    with open("json.txt", "r") as JSONfile:
        JSONobject = json.load(JSONfile)
        for item in JSONobject["marvinArray"]:
            inventory.append(item["item"])

    return inventory

def saveInventory(newItems=None):
    """
    Take a list and save it to a text file if it has less then 4 elements.
    Return boolean.
    """
    returnBool = False
    # Make sure we're not succeeding our maximum space.
    if(newItems != None and len(newItems) < 4):
        with open("inv.data", "w") as inventory_file:
            inventory_file.write("".join(newItems))
            returnBool = True

    return returnBool

def saveJSONInventory(newItems=None):
    """
    Take a list and save it to a JSON file if it has less then 4 elements.
    Return boolean.
    """
    returnBool = False
    # Make sure we're not succeeding our maximum space.
    if(newItems != None and len(newItems) <= 4):
        with open("json.txt", "w") as JSONfile:
            JSONobject = {"marvinArray": []}
            for eachitem in newItems:
                JSONobject["marvinArray"].append({"item": eachitem})
            json.dump(JSONobject, JSONfile, indent=4)
            returnBool = True

    return returnBool

def getInventory():
    """
    Display the number of items and the items in the inventory.
    """
    # Load our inventory.
    inv_list = loadJSONInventory()
    # Count the amount of elemnts using len.
    sumOfItems = len(inv_list)
    result = "\nThere are: %s items in my bag.\n" % sumOfItems

    if sumOfItems > 0:
        # Return the amount of elements and the elements.
        result += "This is what they are called: \n"

        for eachitem in inv_list:
            result += eachitem

    print(result)

def pickItem(item):
    """
    Add the item argument to our inventory.
    """
    # Set default value for result.
    result = "I can't find one."
    # Check if saving went well.
    if saveJSONInventory(loadJSONInventory() + [item + "\n"]):
        result = "\nI've added a %s to my inventory!" % item
    else:
        result = "\nMy inventory is full!\n"

    print(result)


def dropItem(item):
    """
    Drop the provided item in the inventory.
    """
    # Set default value for result and define our list.
    result = "I'm sorry, there is no %s in my inventory." % item
    # Open the inventory file.
    inv_list = loadJSONInventory()
    for i, eachitem in enumerate(inv_list):
        if item in eachitem:
            result = "\n" + item + " has been removed from my inventory."
            # Delete the item from our inventory.
            del inv_list[i]
            # Update the saved inventory.
            saveJSONInventory(inv_list)
            break

    print(result)

def dropEntireInventory():
    """
    Delete marvins inventory by overwriting the file.
    """
    with open("json.txt", "w") as JSONfile:
        JSONfile.write("{\n    \"marvinArray\": [\n\n    ]\n}")

    print("I have thrown away all my items")

"""
Kmom05:

"""
def loadFile(arg_file, lineEndings=True):
    """
    Reads each row in file and puts it in a list.
    arg_file: the file to read.
    lineEnding: false returns a list without the LAST line-ending.
    Returns the list.
    """
    result = []
    with open(arg_file, "r") as inventory_file:
        result = inventory_file.readlines()
        if(lineEndings is False):
            for i, row in enumerate(result):
                result[i] = row[:-1]

    return result

def top7(arg_dict, top7_str="The top 7 are:"):
    """
    Print the 7 most common occurences based on the value as frequency.
    ar_dict, contains the item and the item frequency.
    top7_str, customizable string used when printing.
    """
    # Turn the dictionary into a list of tuples.
    tuple_list = [(k, arg_dict[k]) for k in sorted(arg_dict, key=arg_dict.get, reverse=True)]
    # Initiate resukt with top7_str.
    result = str(top7_str) + "\n"
    for i, item in enumerate(tuple_list):
        if i < 7:
            result += str(i+1) + ". \"" + item[0] + "\" occurs: " + str(item[1]) + " time(s).\n"
        else: break
    print(result)

def wordHistogram(word_list):
    """
    Count the amount of times each word appears, return dictionary.
    """
    d = dict()
    for word in word_list:
        d[word] = d.get(word, 0) + 1
    return d

def charHistogram(char_list):
    """
    Count the amount of times each char appears, return dictionary.
    """
    d = dict()
    for char in char_list:
        d[char] = d.get(char, 0) + 1
    return d

def apostropheRemoval(word_str):
    """
    Check for apostrophes surrounding the word and remove them.
    """
    result = word_str
    if word_str.count("'") > 0:
        if word_str.startswith("'"):
            result = word_str[1:]
        if result.endswith("'"):
            result = result[:-1]

    return result

def analyzeTextfile():
    """
    Finds the number of words and letters in a textfile.
    """
    # Ask for the name of the textfile or use alice-ch1.txt as default.
    fileName = ""
    while True:
        fileName = input("Enter the name of your text file or press \"q\" to quit \n--> ")
        if fileName == "q":
            break
        elif fileName == "":
            fileName = "alice-ch1.txt"
            break
        elif fileName != "":
            break

    # Get the textFile as a list.
    file_list = loadFile(fileName, lineEndings=False)
    # Load dictionary of correctly spelled words.
    correctWords_list = loadFile("words.txt", lineEndings=False)
    # Load all words into a dictionary, using dict comprehension.
    correctWords_dict = {value: i for i, value in enumerate(correctWords_list)}

    # Split it up into words.
    splitWord_list = []
    for row in file_list:
        splitWord_list = splitWord_list + row.split(" ")

    # Remove unwanted characters, line-endings and format words.
    word_list = []
    for word in splitWord_list:
        # Remove non-word characters.
        newWord = re.sub("[^a-zA-Z0-9']", "", word)

        # If word is a valid word, leave it alone.
        if newWord not in correctWords_dict:
            # If word is uppercase.
            if newWord.isupper():
                temp_list = list(newWord)
                # Turn the word into a name/title.
                for i, ch in enumerate(newWord[1:]):
                    temp_list[i+1] = ch.lower()
                # Check if the word is a valid uppercase name/title/word.
                if "".join(temp_list) in correctWords_dict:
                    newWord = "".join(temp_list)
                # Otherwise make it all lowercase and remove apostrophe.
                else:
                    newWord = apostropheRemoval(newWord.lower())
            # Otherwise remove the stray apostrophe from the word.
            else:
                newWord = apostropheRemoval(newWord)

        # Remove empty lines.
        if newWord != "":
            word_list.append(newWord)

    # Print the amount of words.
    print("There are %s words in %s." % (len(word_list), fileName))

    # Count the occurence of all words using a histogram.
    word_dict = wordHistogram(word_list)
    # Print top7 values.
    top7(word_dict, "The 7 most regular words:")

    # Remove the common words and display the 7 most used words.
    # Load common words.
    commonWords_list = loadFile("common-words.txt", lineEndings=False)

    # Remove common words.
    for word in commonWords_list:
        if word in word_dict:
            del word_dict[word]
    # Print the 7 most used words.
    top7(word_dict, "The 7 most used without regular words:")

    # Remove misspelled words.
    temp_dict = dict()
    for word in word_dict:
        if word in correctWords_dict:
            temp_dict[word] = word_dict[word]
    # Print the 7 most used words.
    top7(temp_dict, "The 7 most used, without regular words and with correct spelling:")

    # Create a list of letter.
    char_list = []
    for word in word_list:
        for char in word:
            char_list.append(char)
    # Calculate the most used letter.
    letters_dict = charHistogram(char_list)
    # Print the 7 most used.
    # Turn the dictionary into a list of tuples.
    tuple_list = [(k, letters_dict[k]) for k in sorted(letters_dict, key=letters_dict.get, reverse=True)]
    # Initiate resukt with top7_str.
    result = str("The 7 most used letters are:") + "\n"
    for i, item in enumerate(tuple_list):
        if i < 7:
            result += str(i+1) + ". \"" + item[0] + "\" occurs: " + str(item[1]) + " times"
            result += "(" + str(int((item[1] / len(char_list)) * 100)) + "%)\n"
        else: break
    print(result)
