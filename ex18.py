#!/usr/bin/env python
#
# name: ex18.py
#
"""
A pangram is a sentence that contains all the letters of the English alphabet at least once,
for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function
to check a sentence to see if it is a pangram or not.
"""

def pangram(s):
    s = str(s)
    words_list = s.split()
    chars_list = []
    for word in words_list:
        for char in word:
            if char not in chars_list and char.isalpha():
                chars_list.append(char.lower())
    if len(chars_list) == 26:
        return True
    else:
        return False

if __name__ == '__main__':
    check_string = raw_input('[!] Check string: ')
    print pangram(check_string)
