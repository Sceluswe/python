#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2b2016fea6bde6f296d735d32408503a
python
lab3
emmd12
2016-09-15 11:16:39
v2.2.15 (2016-05-31)

Generated 2016-09-15 13:16:39 by dbwebb lab-utility v2.2.15 (2016-05-31).
https://github.com/mosbth/lab
"""


from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print(">>> Ready to begin.")



"""
==========================================================================
Lab 3 - python



"""



"""
--------------------------------------------------------------------------
Section 1. List basics



"""



"""
Exercise 1.1

Concatenate the two lists [cougar, floor] and [mosquito, bumblebee].

Answer with your list.


Write your code below and put the answer into the variable ANSWER.
"""

myList1 = ['cougar', 'floor']
myList2 = ['mosquito', 'bumblebee']




ANSWER = myList1 + myList2

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2

Use the list [lion, tiger, ozelot, bobcat, cougar].

Add the words 'purple' and 'money' as the second and third element.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["lion", "tiger", "ozelot", "bobcat", "cougar"]

myList.insert(1, "purple")
myList.insert(2, "money")


ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3

Use the list [lion, tiger, ozelot, bobcat, cougar].

Replace the third word with: 'potato'.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["lion", "tiger", "ozelot", "bobcat", "cougar"]

myList[2] = "potato"


ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4

Sort the list

> [wasp, fly, butterfly, bumblebee, mosquito]

in ascending alphabetical order. Answer with the sorted list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]

myList.sort()


ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5

Use the list from the last excercise

> [wasp, fly, butterfly, bumblebee, mosquito]

and sort it in decending alphabetical order. Answer with the sorted list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]

myList.sort(reverse=True)


ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6

Use `pop()` to get the second and the last element in the list:

> [lion, tiger, ozelot, bobcat, cougar]

Answer with the popped elements in a new list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["lion", "tiger", "ozelot", "bobcat", "cougar"]

myNewList = [myList.pop(1), myList.pop()]




ANSWER = myNewList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7

Use `remove()` to delete the word:

> 'piano'

from the list:

> [flute, guitar, drums, piano, bass]

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["flute", "guitar", "drums", "piano", "bass"]

myList.remove("piano")


ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Built-in list functions

Some basic built-in functions.

"""



"""
Exercise 2.1

Use a built-in function to sum all numbers in the list:

> [123, 4, 125, 69, 155]

Answer with the result as an integer.


Write your code below and put the answer into the variable ANSWER.
"""

myList = [123, 4, 125, 69, 155]




ANSWER = sum(myList)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2

Use built-in functions, such as `sum` and `len` to get the average value of
the list:

> [123, 4, 125, 69, 155]

Answer with the result as a float with at most one decimal.


Write your code below and put the answer into the variable ANSWER.
"""

myList = [123, 4, 125, 69, 155]




ANSWER = round(sum(myList) / len(myList), 1)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3

Use a built-in function to get the lowest number in the list:

> [567, 23, 12, 36, 7]

Answer with the result as a integer.


Write your code below and put the answer into the variable ANSWER.
"""

myList = [567, 23, 12, 36, 7]




ANSWER = min(myList)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4

Use the built-in functions `split()` and `join()` to fix this string:

> "The?grass?is?growing"

into a real sentence, (without '?').

Answer with the fixed string.


Write your code below and put the answer into the variable ANSWER.
"""

myString = "The?grass?is?growing"

myList = myString.split("?")

ANSWER = " ".join(myList)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5

Use the string:

> "I have not failed. I've just found 10,000 ways that won't work."

and split it with the delimiter " " (space).

Answer with the element at index 6.


Write your code below and put the answer into the variable ANSWER.
"""

myString = "I have not failed. I've just found 10,000 ways that won't work."

myList = myString.split(" ")

ANSWER = myList[6]

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6

Use slice on the list

> [dvd, mp3, blu-ray, vhs, cd]

and replace the second and third element with

> "freezer, fridge"

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["dvd", "mp3", "blu-ray", "vhs", "cd"]

myList[1:3] = ["freezer", "fridge"]


ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
Exercise 2.7

Use slice on the list

> [dvd, mp3, blu-ray, vhs, cd]

and replace the last two elements with

> "freezer, fridge"

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["dvd", "mp3", "blu-ray", "vhs", "cd"]

myList[-2:] = ["freezer", "fridge"]


ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.7", ANSWER, False))

"""
Exercise 2.8

Use slice on the list

> [dvd, mp3, blu-ray, vhs, cd]

and insert the words

> "freezer, fridge"

after the third element.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["dvd", "mp3", "blu-ray", "vhs", "cd"]


myList[3:3] = ["freezer", "fridge"]

ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.8", ANSWER, False))

"""
Exercise 2.9

Use `del` on the list

> [tree, stone, grass, water, sky]

and delete the first element.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["tree", "stone", "grass", "water", "sky"]

del myList[0]


ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.9", ANSWER, False))

"""
Exercise 2.10

Use `del` on the list

> [tree, stone, grass, water, sky]

and delete the second and third element.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["tree", "stone", "grass", "water", "sky"]

del myList[1:3]


ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.10", ANSWER, False))

"""
Exercise 2.11

Assign the list

> [b, a, e, d, c]

to a variable called 'list1'.

Assign the list again, but to another variable called 'list2'.

Answer with the result of 'list1 is list2'.


Write your code below and put the answer into the variable ANSWER.
"""

list1 = ["b", "a", "e", "d", "c"]
list2 = ["b", "a", "e", "d", "c"]



ANSWER = list1 is list2

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.11", ANSWER, False))

"""
Exercise 2.12

Use your lists from the last exercise. Assign 'list1' to another variable
called 'list3' like this:

> list3 = list1

Answer with the result of 'list1 is list3'.


Write your code below and put the answer into the variable ANSWER.
"""

list3 = list1




ANSWER = list1 is list3

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.12", ANSWER, False))

"""
Exercise 2.13

Use your lists from the last exercise. Change the first element in 'list1'
to

> "p"

Answer with 'list3'.


Write your code below and put the answer into the variable ANSWER.
"""

list1[0] = "p"




ANSWER = list3

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Lists as arguments

Some excercises with passing lists as arguments to a function.

"""



"""
Exercise 3.1

Create a function that returns the list passed as argument sorted in
numerical and ascending order. Also multiply all values with 10.

Use the list:

> [567, 23, 12, 36, 7]

and the built-in method `sort()`.

Answer with the sorted list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = [567, 23, 12, 36, 7]

def sortAndMultiply(the_list):
    """
    Multiply all numbers by 10 and sort the list.
    """
    the_list.sort()

    for i, eachnumber in enumerate(the_list):
        the_list[i] = eachnumber * 10

    return the_list

ANSWER = sortAndMultiply(myList)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2

Create a function that takes the list:

> [123, 4, 125, 69, 155]

as argument.

The function should multiply all even numbers by 3 and add 7 to all odd
numbers.

Answer with the modified list sorted in numerical order, descending.


Write your code below and put the answer into the variable ANSWER.
"""

def increaseNumbers(the_list):
    """
    Multiply even numbers by 3 and add 7 to odd ones.
    """
    for index, eachnumber in enumerate(the_list):
        if(eachnumber % 2 == 0):
            the_list[index] = the_list[index] * 3
        elif(eachnumber % 2 != 0):
            the_list[index] = the_list[index] + 7

    the_list.sort(reverse=True)

    return the_list


ANSWER = increaseNumbers([123, 4, 125, 69, 155])

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))


dbwebb.exitWithSummary()
