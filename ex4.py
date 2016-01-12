#!/usr/bin/python
#
# name: ex4.py
#
"""
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
"""
import ex3
from sys import argv
def vowel_check(x):
    if not ex3.str_length(x) == 1:
        print "[!] Oops, \"%s\" too long. Exit." %(x)
        exit()
    if x in "aeiou":
        return True
    else:
        return False

if __name__ == "__main__":
    script, check_char = argv
    check = vowel_check(check_char)
    print "[+] \"%s\" is vowel:" %(check_char), check