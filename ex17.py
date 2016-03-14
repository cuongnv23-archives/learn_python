#!/usr/bin/env python
#
# name: ex17.py
#
"""
Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.",
"Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil",
"Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir",
or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.
"""

from ex8 import is_palindrome

def palindromes_check(s):
    s = str(s)
    temp_split = s.split()
    temp_check = ''
    for e in temp_split:
        i = len(e)
        for j in e[0:i]:
            if j.isalpha():
                temp_check += j.lower()
    return is_palindrome(temp_check)

if __name__ == '__main__':
    check_str = raw_input('[+] The check string: ')
    print "Palinkdromes: ", palindromes_check(check_str)