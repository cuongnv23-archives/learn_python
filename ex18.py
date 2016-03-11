#A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.

#!/usr/bin/python

import string

def is_pangram(inp):
    pangram = 0
    alp = string.ascii_lowercase

    for i in alp:
        if i not in inp:
            pangram = pangram + 1

    if pangram == 0:
        return True
    else:
        return False

print is_pangram(raw_input('Enter a sentence: '))
