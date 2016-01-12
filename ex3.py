#!/usr/bin/python
#
# name: ex3.py
"""
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exer
"""
from sys import argv

def str_length(x):
    x = str(x)
    count = 0
    for c in x:
        count += 1
    return count
if __name__ == "__main__":
    script, input_string = argv
    print "[+] String: %s - Lengh: %d" %(input_string,str_length(input_string))

