#!/usr/bin/env python
#
#
"""
1. Define a function max() that takes two numbers as arguments and returns the largest of them.
Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
"""

# Find out the higher number from 2 integer numbers
def max(x, y):
    # Trying to force checking the input number
    try:
        x = int(x)
        y = int(y)
    except ValueError as msg:
        print("[!] Oops, invalid input number. Used for integer only. \n\
Msg: %s" %(msg))
        exit()
    # Compare
    if x > y:
        return x
    else:
        return y

# The main function
if __name__ == "__main__":
    x = raw_input("[+] The first number: ")
    y = raw_input("[+] The second number: ")
    print("[!] The higher number: %d" %(max(x, y)))