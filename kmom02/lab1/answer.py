#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
24e781135a78afca12aea903f5f8a8d2
python
lab1
emmd12
2016-08-29 09:09:10
v2.2.15 (2016-05-31)

Generated 2016-08-29 11:09:11 by dbwebb lab-utility v2.2.15 (2016-05-31).
https://github.com/mosbth/lab
"""


from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print(">>> Ready to begin.")



"""
==========================================================================
Lab 1 - python 
 
If you need to peek at examples or just want to know more, take a look at
the [Python manual](https://docs.python.org/3/library/index.html).

There you will find everything this lab will go through and much more.
 
"""



"""
--------------------------------------------------------------------------
Section 1. Integers, strings, floats and basic arithmetics 
 
The foundation of numbers and basic arithmetic.
 
"""



"""
Exercise 1.1 
 
Create a variable called 'numOne' and give it the value 91. Create another
variable called 'numTwo' and give it the value 70. Create a third variable
called 'result' and assign to it the sum of the first two variables.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

numOne = 91
numTwo = 70
result = numOne + numTwo

ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Create a variable called 'numThree' and give it the value 100. 

Create another variable called 'numFour' and give it the value 67. 

Subtract 'numThree' from 'numFour' and answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

numThree = 100
numFour = 67
result = numFour - numThree


ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Find out the product of 'numOne' and 'numThree' and answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

result = numOne * numThree




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Divide 30 with 5 and answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

result = 30 / 5




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Create a variable called 'floatOne' and give it the value 51.3. 

Create another variable called 'floatTwo' and give it the value 52.27.

Sum the two values and answer with the result, rounded to 2 decimals.
 

Write your code below and put the answer into the variable ANSWER.
"""

floatOne = 51.3
floatTwo = 52.27
result = round((floatOne + floatTwo), 2)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Subtract 'floatTwo' from 'floatOne' and answer with the result. Round to 2
decimals.
 

Write your code below and put the answer into the variable ANSWER.
"""

result = round(floatOne - floatTwo, 2)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Answer with the product of 'floatOne' and 'floatTwo', rounded to 4
decimals.
 

Write your code below and put the answer into the variable ANSWER.
"""

result = round(floatOne * floatTwo, 4)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Create three variables: 'n1' = 172, 'n2' = 309 and 'n3' = 74. Sum up 'n1'
and 'n2'. Subtract 'n3' and answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

n1 = 172
n2 = 309
n3 = 74
result = (n1 + n2) - n3




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Answer with the result of 186 modulo (%) 88.
 

Write your code below and put the answer into the variable ANSWER.
"""

result = 186 % 88




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10 
 
Add the word: 'error' to the word: 'barbeque' and answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

result = "barbeque" + "error"




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Conditions, exceptions, booleans, if, else and elif 
 

 
"""



"""
Exercise 2.1 
 
Answer with the boolean value of: 451 is less than 192.
 

Write your code below and put the answer into the variable ANSWER.
"""

result = 451 < 192




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Answer with the boolean value of: 114 is larger than 342.
 

Write your code below and put the answer into the variable ANSWER.
"""

result = 114 > 342




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Answer with the boolean value of: 451 == 114.
 

Write your code below and put the answer into the variable ANSWER.
"""

result = 451 == 114




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Create three variables representing dice values: 'd1' = 1, 'd2' = 6 and
'd3' = 1. Sum them up and answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

d1 = 1
d2 = 6
d3 = 1
diResult = d1 + d2 + d3




ANSWER = diResult

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Create an if statement to see if the total value of your dices is 11 or
higher. If that is the case, answer with the string: 'big', else answer
with the string: 'nothing'. 
 

Write your code below and put the answer into the variable ANSWER.
"""

if(diResult >= 11):
    result = "big"
else:
    result = "nothing"




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6 
 
Create an elif statement that checks your total dice value. The checks and
results should be: three of the same value = 'triple', total of 11 or
higher = 'big', total of 10 or lower = 'small'. If you get a triple you
should not make more checks.
 

Write your code below and put the answer into the variable ANSWER.
"""

if(d1 == d2 and d2 == d3):
    result = "triple"
elif(diResult >= 11):
    result = "big"
elif(diResult <= 10):
    result = "small"




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Built-in functions 
 
Some useful built-in functions.
 
"""



"""
Exercise 3.1 
 
Use `max()` to find the largest number in the serie:
6,8,95,2,12,152,4,78,621,45. 

Answer with the result. 
 

Write your code below and put the answer into the variable ANSWER.
"""

result = max([6, 8, 95, 2, 12, 152, 4, 78, 621, 45])




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2 
 
Use `min()` to find the smallest number in the serie:
6,8,95,2,12,152,4,78,621,45.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

result = min([6, 8, 95, 2, 12, 152, 4, 78, 621, 45])




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))

"""
Exercise 3.3 
 
Use `len()` to find the number of letters in the word: input.

Answer with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

result = len("input")




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.3", ANSWER, False))

"""
Exercise 3.4 
 
Convert the number 697 to a string and add it to the word 'input'. Answer
with the result.
 

Write your code below and put the answer into the variable ANSWER.
"""

result = "input" + str(697)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.4", ANSWER, False))

"""
Exercise 3.5 
 
Convert the number 711.98 to an integer and then to a string. Add it to the
beginning of the word: 'input'. Answer with the result. 
 

Write your code below and put the answer into the variable ANSWER.
"""

result = str(int(711.98)) + "input"




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.5", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 4. Functions 
 
Basic functions.
 
"""



"""
Exercise 4.1 
 
Create a function called 'prodNr' that takes two arguments, 40 and 32. The
function should return the product of the numbers.

Answer with a call to the function. 
 

Write your code below and put the answer into the variable ANSWER.
"""

def prodNr(num1, num2):
    """
    Returns the product of the two parameters.
    """
    return num1 * num2


ANSWER = prodNr(40, 32)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("4.1", ANSWER, False))

"""
Exercise 4.2 
 
Create a function called 'funnyWord' that takes one argument and adds it to
the string ' is a funny word'. If the argument is 'water', the function
should return: 'water is a funny word'.

Use the argument 'water' and answer with a call to the function.
 

Write your code below and put the answer into the variable ANSWER.
"""

def funnyWord(concstr):
    """
    Concatenates the parameter to a string.
    """
    return concstr + " is a funny word"


ANSWER = funnyWord("water")

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("4.2", ANSWER, False))

"""
Exercise 4.3 
 
Create a function called 'inRange' that takes one argument. The function
should return 'true' if the argument is higher than 50 and lower than 100.
If the number is out of range, the function should return 'false'. The
return type should be boolean.

Use the argument 80 and answer with a call to the function.
 

Write your code below and put the answer into the variable ANSWER.
"""

def inRange(number):
    """
    Returns true if a number is within the range 50-100 or false it not.
    """
    boolean = False
    
    if(number > 50 and number < 100):
        boolean = True
    
    return boolean


ANSWER = inRange(80)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("4.3", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 5. Iteration and loops 
 
For-loops and while-loops. 
 
"""



"""
Exercise 5.1 
 
Create a while-loop that adds 3 to the number 57, 58 times. Answer with the
result. 
 

Write your code below and put the answer into the variable ANSWER.
"""
ex51 = 57
iterator = 0
while(iterator < 58):
    ex51 = ex51 + 3
    iterator = iterator + 1
    

ANSWER = ex51

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.1", ANSWER, False))

"""
Exercise 5.2 
 
Create a while-loop that subtracts 5 from 53, 67 times. Answer with the
result. 
 

Write your code below and put the answer into the variable ANSWER.
"""

ex52 = 53
iterator = 0

while(iterator < 67):
    ex52 = ex52 - 5
    iterator = iterator + 1


ANSWER = ex52

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.2", ANSWER, False))

"""
Exercise 5.3 
 
Create a for-loop that counts the number of elements in the serie:

> 6,8,95,2,12,152,4,78,621,45

Answer with the result. 
 

Write your code below and put the answer into the variable ANSWER.
"""
result = 0
for num in [6, 8, 95, 2, 12, 152, 4, 78, 621, 45]:
    result = result + 1




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.3", ANSWER, False))

"""
Exercise 5.4 
 
Create a for-loop that sums up the numbers in the serie:

> 67,2,12,28,128,15,90,4,579,450

Answer with the result. 
 

Write your code below and put the answer into the variable ANSWER.
"""
result = 0
for num in [67, 2, 12, 28, 128, 15, 90, 4, 579, 450]:
    result = result + num




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.4", ANSWER, False))

"""
Exercise 5.5 
 
Create a for-loop that finds the largest number in the serie:

> 6,8,95,2,12,152,4,78,621,45

Answer with the result. 
 

Write your code below and put the answer into the variable ANSWER.
"""
myArr = [6, 8, 95, 2, 12, 152, 4, 78, 621, 45]
largestnum = myArr[0]

for num in myArr:
    if(largestnum < num):
        largestnum = num




ANSWER = largestnum

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.5", ANSWER, False))

"""
Exercise 5.6 
 
Create a for-loop that goes through the numbers:

> 67,2,12,28,128,15,90,4,579,450

If the current number is even, you should add it to a variable and if the
current number is odd, you should subtract it from the variable.

Answer with the final result. 
 

Write your code below and put the answer into the variable ANSWER.
"""

result = 0

for num in [67, 2, 12, 28, 128, 15, 90, 4, 579, 450]:
    if(num % 2 == 0):
        result = result + num
    elif(num % 2 != 0):
        result = result - num

ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.6", ANSWER, False))


dbwebb.exitWithSummary()
