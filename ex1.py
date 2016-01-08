#Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct #available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good #exercise.)

#!/usr/bin/python

def max(a, b):
    if a > b:
        return a
    else:
        return b
num_1 = raw_input('Input first number: ')
num_2 = raw_input('Input second number: ')

print "The largest one is ",max(int(num_1), int(num_2))
