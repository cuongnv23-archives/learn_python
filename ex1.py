#Define a function max() that takes two numbers as arguments and returns the largest of them.
#Use the if-then-else construct #available in Python.
#(It is true that Python has the max() function built in, but writing it yourself is nevertheless a good #exercise.)

#!/usr/bin/python

from sys import argv

script, num_1, num_2 = argv

def max(a, b):
    if a > b:
        return a
    else:
        return b

print "Max number: ", max(int(num_1), int(num_2))
