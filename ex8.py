#!/usr/bin/env python
#
# name: ex8.py
"""
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
For example, is_palindrome("radar") should return True.
"""


from sys import argv
from ex7 import reverse

def is_palindrome(input_string):
    if reverse(input_string) == input_string:
        return True
    else:
        return False

if __name__ == '__main__':
    try:
        script, input_string = argv
        print '[+] Input: ', input_string
        print '[+] Palindrome check: ', is_palindrome(input_string)
    except ValueError as msg:
        print '[!] Oops, error: %s' %msg

