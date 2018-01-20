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
#
10 * 2 
#
35 / 5
#

35 / 4
#
35 // 4 
#
# What is the difference between the / operator and the // operator?
# 

2 ** 5 
#
# What does the ** operator do?
#
5 % 3 
#
5 % 2
#
5 % 4
#
# What does the % operator do?
#

(1 + 3) * 2
#
# What effect do the parenthesis have on this statement?
#

# Data in python is of different flavors or "types," each with its own characteristics
type(3)
#
type(3.0)
#
type("word")
#
type(True)
#
type(False)
#
type(None)
#
# None is a special object in python. We will talk more about it later


# It is possible to convert from one type to another. 
int(3.0)
#
float(7)
#
str(55)
#
bool(1)
#
# How can you tell the difference between these four different types?
#

# Strings are created with single or double-quotes
"This is a string."
'This is also a string.'

"Hello " + "world!"
# What does the + operator do here?
#

"This is a string"[0]
#
"This is a string"[5]
#
"This is a string"[8]
#
# What is happening as you change the number?
#

"This is a string"[-1]
#
# What happens when you use a negative number?
#

"%s can be %s" % ("strings", "interpolated")
# What is happening here? 
#

# A more robust (and modern) way to put things into strings is using the format method
"{0} can be {1}".format("strings", "formatted")
#

# You can use names instead of numbers to make it easier to keep things straight
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
#

# You have already met the print method
print("I'm Python. Nice to meet you!")
# Here is its sibling, the input method
n = input("What is your name? ")
print("Hello, " + n)
#
# What just happened?
# 

# For your next assignment, you will need to use random numbers 
# first we need to get a few methods from the library called random
from random import random,randint,shuffle,sample
random()
# Run this line a few times. What is happening here?
# 

randint(1,100)
# How is this different?
#

# The next few use a list of numbers from 0 to 9
items = [0, 1,2,3,4,5,6,7,8,9]
shuffle(items)
print(items)
# What just happened?
# 

print(sample(items, 1))
# What does this do?
# 

print(sample(items, 5))
# What does the second parameter control?
# 

for i in range(0,5):
	print(i)
# 
# What is happening here? What happens if you change the two range parameters?
#
