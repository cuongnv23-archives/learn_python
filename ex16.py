#!/usr/bin/env python
#
# name: ex16.py
#
"""
16. Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
"""

def filter_long_words(n, list_of_words):
    result = []
    split_words = str(list_of_words).split()
    for e in split_words:
        if len(e) > n and e not in result:
            result.append(e)
    return result

if __name__ == '__main__':
    check_list = raw_input('[+] Enter string for checking: ')
    limiter = int(raw_input('[+] Minimum length: '))
    print filter_long_words(limiter, check_list)