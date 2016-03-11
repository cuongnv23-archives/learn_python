#!/usr/bin/env python
#
# name: ex15.py
#
"""
15. Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
"""
from ex14 import *
from ex13 import *

def find_longest_word(list_of_words):
    length_map = words_mapping(list_of_words)
    return max_in_list(length_map)

if __name__ == '__main__':
    check_list = raw_input('[+] Enter string to check: ')
    print '[+] The longest word: %d char(s)' %(find_longest_word(check_list))
