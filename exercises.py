'''

01a Exercises
These exercises should help you get the flavor of how to perform arithmetic and string operations in Python. 
You will also get to play with (pseudo-)random generators and the range operator.
These skills will all be used in assignment 2.

To answer these exercises, open the IDLE program that came with your Python installation. IDLE is a line-by-line Python interpreter.
You can copy lines from this file into IDLE to interpret them and produce a result. Then copy the result back to the following line in this file (after the #).
You will also need to answer several questions to show you understand what is happening. 


'''
# Math in Python is what you would expect. Add comments with the answers the IDLE returns. I'll do the first one for you.
10 + 15 
#25
8 - 1 
#7
10 * 2 
#20
35 / 5
#7

35 / 4
#8.75
35 // 4 
#8
# What is the difference between the / operator and the // operator?
# the / operator divides a the number on the left by the number on the right, the // operator does something else that Im unsure of. Its still math whatever it is, but whatever it was I wasnt taught it before. I looked it up after I wrote down this and found out it is something called floor dvision

2 ** 5 
#32
# What does the ** operator do?
# This I do know, it does powers...like 2 to the power of 5.
5 % 3 
#2
5 % 2
#1
5 % 4
#1
# What does the % operator do?
#No idea

(1 + 3) * 2
#8
# What effect do the parenthesis have on this statement?
#the equation in the parenthesis is calculated and then that caclulated number is used in the full equation

# Data in python is of different flavors or "types," each with its own characteristics
type(3)
#<class 'int'>
type(3.0)
#<class 'float'>
type("word")
#<class 'str'>
type(True)
#<class 'bool'>
type(False)
#<class 'bool'>
type(None)
#<class 'NoneType'>
# None is a special object in python. We will talk more about it later


# It is possible to convert from one type to another. 
int(3.0)
#3
float(7)
#7.0
str(55)
#'55'
bool(1)
#True
# How can you tell the difference between these four different types?
#They modify the numbers presentation in a certain way that is unique, plus the boo1 just gives out "true" instead of a number

# Strings are created with single or double-quotes
"This is a string."
'This is also a string.'

"Hello " + "world!"
# What does the + operator do here?
#adds the two parts together to create a frankenstein sentence.

"This is a string"[0]
#'T'
"This is a string"[5]
#'i'
"This is a string"[8]
#'a'
# What is happening as you change the number?
# A different letter pops up.

"This is a string"[-1]
#'g'
# What happens when you use a negative number?
# We still get a letter

"%s can be %s" % ("strings", "interpolated")
# What is happening here? 
#The two words in the parenthesis show up in order with the percentage signs with the s at the end, so since strings is the first word it goes first

# A more robust (and modern) way to put things into strings is using the format method
"{0} can be {1}".format("strings", "formatted")
#'strings can be formatted'

# You can use names instead of numbers to make it easier to keep things straight
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
#'Bob wants to eat lasagna'

# You have already met the print method
print("I'm Python. Nice to meet you!")
# Here is its sibling, the input method
n = input("What is your name? ")
print("Hello, " + n)
#
# What just happened?
# There was a syntax error that found multiple statements while compiling a single statement

# For your next assignment, you will need to use random numbers 
# first we need to get a few methods from the library called random
from random import random,randint,shuffle,sample
random()
# Run this line a few times. What is happening here?
# I keep getting syntax errors.

randint(1,100)
# How is this different?
#Instead of the multiple statements found when compiling it tells me that randint is not defined, a name error

# The next few use a list of numbers from 0 to 9
items = [0, 1,2,3,4,5,6,7,8,9]
shuffle(items)
print(items)
# What just happened?
#  While Items was accepted, the shuffle code did not work....The print item did though, and listed the items in order.

print(sample(items, 1))
# What does this do?
# More Namerrors

print(sample(items, 5))
# What does the second parameter control?
#  The second parameter is supposed to give me supposedly 5 random numbers, but it doesnt due to NamErrors

for i in range(0,5):
	print(i)
# 
# What is happening here? What happens if you change the two range parameters?
# This code actually works, and gives me 5 numbers counting up from zero to four, aka the fifth number in the base ten counting method. the number on the right is the xth number in base ten it counts to, while the left is the number it starts from
