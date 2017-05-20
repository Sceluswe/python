#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
e4a4f3918dfa6e9a7589ec0d97f9be09
python
lab4
emmd12
2016-10-03 15:42:58
v2.2.20 (2016-09-29)

Generated 2016-10-03 17:42:58 by dbwebb lab-utility v2.2.20 (2016-09-29).
https://github.com/mosbth/lab
"""


from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print(">>> Ready to begin.")



"""
==========================================================================
Lab 4 - python

Dictionaries and tuples.

"""



"""
--------------------------------------------------------------------------
Section 1. Dictionaries

Some basics with dictionaries.

"""



"""
Exercise 1.1

Create a small phonebook using a dictionary. Use the names as keys and
numbers as values.

Use

> Chandler, Monica, Ross

and corresponding numbers

> 55523645, 55564452, 55545872

Add the phonenumbers as integers. Answer with the resulting dictionary.


Write your code below and put the answer into the variable ANSWER.
"""

phonebook_dict = {"Chandler": 55523645, "Monica": 55564452, "Ross": 55545872}




ANSWER = phonebook_dict

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2

How many items are there in the dictionary?


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = len(phonebook_dict)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3

Use the `get()` method on your phonebook and answer with the phonenumber of
'Ross'.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = phonebook_dict.get("Ross", 0)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4

Get all keys from the dictionary and return them in a sorted list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = []
for key in phonebook_dict:
    myList.append(key)




ANSWER = sorted(myList)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5

Get all values from the dictionary and return them in a sorted list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = []
for key in phonebook_dict:
    myList.append(phonebook_dict[key])




ANSWER = sorted(myList)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6

Use the in-operator to test if the name 'Ross' exists in the dictionary.
Answer with the return boolean value.


Write your code below and put the answer into the variable ANSWER.
"""






ANSWER = "Ross" in phonebook_dict

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7

Use the in-operator to test if the phone number 55545872 exists in the
dictionary. Answer with the return boolean value.


Write your code below and put the answer into the variable ANSWER.
"""




ANSWER = 55545872 in phonebook_dict.values()

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8

Use a for-loop to walk through the dictionary and create a string
representing it. Each name and number should be on its own row, separated
by a space. The names must come in alphabetical order.

Answer with the resulting string.


Write your code below and put the answer into the variable ANSWER.
"""

str_dictRepresentation = ""

# Use DSU.
# Decorate.
myList = phonebook_dict.items()

# Sort.
myList = sorted(myList)

# Undecorate.
for name, number in myList:
    str_dictRepresentation += name + " " + str(number) + "\n"




ANSWER = str_dictRepresentation

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9

Convert the phonenumber to a string and add the prefix '+1-', representing
the language code, to each phone-number.

Answer with the resulting dictionary.


Write your code below and put the answer into the variable ANSWER.
"""
result_dict = {}
for key in phonebook_dict:
    result_dict[key] = '+1-' + str(phonebook_dict[key])




ANSWER = result_dict

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10

Get and remove the item 'Ross' from the phonebook (use pop()). Answer with
the resulting dictionary.


Write your code below and put the answer into the variable ANSWER.
"""

phonebook_dict.pop("Ross")




ANSWER = phonebook_dict

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, True))

"""
Exercise 1.11

Add the item you just popped from the phonebook. Answer with the resulting
dictionary.


Write your code below and put the answer into the variable ANSWER.
"""

phonebook_dict['Ross'] = 55545872




ANSWER = phonebook_dict

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Tuples

Some basics with tuples.

"""



"""
Exercise 2.1

Create a tuple with 'bear, 65, 6.47, chair, 5'. Answer with the length of
the tuple as an integer.


Write your code below and put the answer into the variable ANSWER.
"""

bearChair_tuple = ('bear', 65, 6.47, 'chair', 5)




ANSWER = len(bearChair_tuple)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2

Create a tuple out of:

> (bear, 65, 6.47, chair, 5).

Assign each value in the tuple to different variables:

> 'a','b','c','d','e'.

Answer with the variable: 'd'. Hint: a,b,c = tuple.


Write your code below and put the answer into the variable ANSWER.
"""

a, b, c, d, e = ('bear', 65, 6.47, 'chair', 5)




ANSWER = d

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3

Use the list

> [567, 23, 12, 36, 7]

Assign the first two elements to a tuple with a slice on the list.

Answer with the first element in the tuple as an integer.


Write your code below and put the answer into the variable ANSWER.
"""
myList = [567, 23, 12, 36, 7]
myTuple = tuple(myList[:3])




ANSWER = myTuple[0]

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4

Create a tuple with

> (moose, 12, 1.98, table, 7)

Convert it to a list and replace the second element with:

> "elephant"

Convert it back to a tuple and answer with the first three elements in a
comma-separated string.


Write your code below and put the answer into the variable ANSWER.
"""
myTuple = ('moose', 12, 1.98, 'table', 7)
myList = list(myTuple)
myList[1] = 'elephant'
myTuple = tuple(myList)


ANSWER = str(myTuple[0]) + "," + str(myTuple[1]) + "," + str(myTuple[2])

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))


dbwebb.exitWithSummary()
