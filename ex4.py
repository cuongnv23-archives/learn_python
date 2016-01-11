#
#Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
#
#

#!/usr/bin/python

def check_vowel(c):
    if (len(c) == 1) and (c in "a u e i o"):
        return True
    else:
        return False

char = raw_input('Enter 1 character: ')

if check_vowel(char):
    print "True"
else:
    print "False"
