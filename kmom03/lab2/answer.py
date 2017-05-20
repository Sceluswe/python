#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
dd98b038379a7be555cc46d56f85d13b
python
lab2
emmd12
2016-08-31 14:19:16
v2.2.15 (2016-05-31)

Generated 2016-08-31 16:19:17 by dbwebb lab-utility v2.2.15 (2016-05-31).
https://github.com/mosbth/lab
"""


from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print(">>> Ready to begin.")



"""
==========================================================================
Lab 2 - python 
 
Strings and files.
 
"""



"""
--------------------------------------------------------------------------
Section 1. Strings 
 
The basics of strings.
 
"""



"""
Exercise 1.1 
 
Assign the word: 'candy' to a variable and put your variable as the answer.
 

Write your code below and put the answer into the variable ANSWER.
"""

myCandy = "candy"




ANSWER = myCandy

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Assign the word 'candy' to a variable. Create another variable where you
put the first and the last letter in the word.

Answer with the second variable.
 

Write your code below and put the answer into the variable ANSWER.
"""

myCandy = "candy"
strAnswer = myCandy[0] + myCandy[-1:] 




ANSWER = strAnswer

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Assign the word: helicopter to a variable. Answer with the length of the
word as an integer.
 

Write your code below and put the answer into the variable ANSWER.
"""

myHeli = "helicopter"




ANSWER = len(myHeli)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Use the 'in-operator' to see if the word: 'plane' contains the letter 'a'.
Answer with a boolean result.
 

Write your code below and put the answer into the variable ANSWER.
"""

result = "a" in "plane"




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Make all the letters in the word 'helicopter' capitalized. Answer with the
capitalized word.
 

Write your code below and put the answer into the variable ANSWER.
"""

myHeli = "helicopter"




ANSWER = myHeli.upper()

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Use the built-in function `startswith()` to see if the word 'soda' starts
with the letter 'o'. Answer with the boolean value.
 

Write your code below and put the answer into the variable ANSWER.
"""

mySoda = "soda"




ANSWER = mySoda.startswith("o")

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Assign the words: 'cake' and 'cake' to two different variables. 

Create a function and pass the two words as arguments to it. Your function
should return them as a single word.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

cake1 = "cake"
cake2 = "cake"

def concTwoStr(str1, str2):
    """
    Concatenate two srings and return them.
    """
    return str1 + str2


ANSWER = concTwoStr(cake1, cake2)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Create a function and pass the word: 'candy' to it. Your function should
return the sentence:

> "This word was: candy"

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

myCandy = "candy"

def myWord(str1):
    """
    Concatenate a string argument with a predefined string.
    """
    return "This word was: " + str1



ANSWER = myWord(myCandy)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Create a function and pass the word: 'cake' to it.

Your function should return the string 'yes' if the word is longer than 5
characters. Else return 'no'.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

myCake = "cake"

def lenOverFive(str1):
    """
    Check if a string is longer than 5 characters.
    """
    myLength = "no"
    
    if(len(str1) > 5):
        myLength = "yes"
    
    return myLength

    
ANSWER = lenOverFive(myCake)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10 
 
Create a function and pass the word: 'helicopter' to it.

Your function should return a string with the word backwards.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""
myHeli = "helicopter"

def backwardsStr(str1):
    """
    Turn the string backwards.
    """
    return str1[::-1]




ANSWER = backwardsStr(myHeli)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
Exercise 1.11 
 
Create a function and pass the word: 'cake' to it.

Your function should exclude the first and the last letter of the word and
return it.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

myCake = "cake"

def strMiddle(str1):
    """
    Exclude the first and last letters of a word.
    """
    return str1[1:-1]



ANSWER = strMiddle(myCake)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
Exercise 1.12 
 
Use `str.format()` to print out:

> 'My 'string' has 'integer' 'string''.

Use the values: 'book', '398' and 'pages'. Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

myString = "My {string1} has {integer} {string2}"




ANSWER = myString.format(string1="book", integer=398, string2="pages")

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.12", ANSWER, False))

"""
Exercise 1.13 
 
Use `find` and `slice` on the string:

> "789.234.2.54 : (sunshine), bakery"

to get the word inside the parenthesis.

Answer with the word as a string.
 

Write your code below and put the answer into the variable ANSWER.
"""

myString = "789.234.2.54 : (sunshine), bakery"

myStartSlice = myString.find("(") + 1
myEndSlice = myString.find(")")

myString = myString[myStartSlice:myEndSlice]


ANSWER = myString

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Files 
 
This section uses the text file: '[httpd-access.txt](httpd-access.txt)'.
 
"""



"""
Exercise 2.1 
 
Open the file and count the number of times a line starts with '81'. Answer
with the result as an integer.
 

Write your code below and put the answer into the variable ANSWER.
"""

myFile = open("httpd-access.txt", "r")

count = 0

for line in myFile:
    if(line.startswith("81")):
        count = count + 1 
        
myFile.close()


ANSWER = count

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Find out the last 4 digits on line 821 in the file. Answer with the result
as an integer.
 

Write your code below and put the answer into the variable ANSWER.
"""

myFile = open("httpd-access.txt", "r")

# Set count to 1, because the first line we read, is the first line!
# In this example we do not want the first line to have the index 0.
# If it does then line 821 in the file would become 820 in our loop.
# I could also chose to change count before the if statement. But 
# that would lead to trouble (we would skip an elemnt) should we 
# be iterating through a list.
# It is best to get used to increasing the iterator last of all.
count = 1
line821 = ""

# Get the line in question.
for line in myFile:
    
    # Check for the specific line.
    if(count == 821):
        line821 = line
        # break because we've found our line.
        break
        
    # Increase iterator
    count = count + 1

# Here count MUST be 0 because we're looping through a string as if  
# it is a list/array. The first index of an array is ALWAYS 0.
count = 0
numericChars = ""
# Collect all digits from a line.
while(count < len(line821)):
    if(line821[count].isnumeric()):
        numericChars = numericChars + line821[count]
    count = count + 1
    
# Close the file for good-practice.
myFile.close()
    
# I chose to solve the problem in this more complicated way so that it would be right
# 100% of the time no matter where the four last digits are on a line.

ANSWER = int(numericChars[-4:])

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Find out which of the ip adresses 81.226.253.26 and 95.19.133.73 that has
the highest amount of entries in the file.

Answer with the result as an integer.
 

Write your code below and put the answer into the variable ANSWER.
"""

myFile = open("httpd-access.txt", "r")

# Define counters.
ip1 = 0
ip2 = 0
result = 0

for line in myFile:
    if(line.startswith("81.226.253.26")):
        ip1 = ip1 + 1
    elif(line.startswith("95.19.133.73")):
        ip2 = ip2 + 1
        
if(ip1 > ip2):
    result = ip1
else:
    result = ip2
    
myFile.close()

ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Count the number of periods (.) there are in the file.

Use the built-in function `count()` on the file after you have converted it
to a string.

Answer with the result as an integer.
 

Write your code below and put the answer into the variable ANSWER.
"""
myString = open("httpd-access.txt", "r").read()

nrOfDots = myString.count(".")

ANSWER = nrOfDots

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Find the characters on line 637 from index 65 to index 75. Make sure that
the character at index 75 also gets included.

Answer with the piece of string you found.
 

Write your code below and put the answer into the variable ANSWER.
"""
# Open file.
myFile = open("httpd-access.txt", "r")
# Declare counter.
count = 1
line637 = ""

# Find line 637
for line in myFile:
    if(count == 637):
        line637 = line
    count = count + 1

# Close file for good-practice.
myFile.close()

ANSWER = line637[65:76]

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6 
 
Find the last element (digit) on each line, if there are any, and sum all
that are even.

Answer with the result as an integer.
 

Write your code below and put the answer into the variable ANSWER.
"""
myFile = open("httpd-access.txt", "r")

result = 0

for line in myFile:
    if(line[-2:-1].isnumeric() and int(line[-2:-1]) % 2 == 0):
        result = result + int(line[-2:-1])
        
        
ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))


dbwebb.exitWithSummary()
