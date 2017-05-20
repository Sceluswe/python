"""
Does shit.
"""
import re

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



def analyze():
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
