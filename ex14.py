#!/usr/bin/python
#Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
def str_len(s):
    s = s.split(' ')
    for i in s:
        print "%s: %d" % (i, len(i))
st = raw_input('Enter a list of word separated by a space: ')
str_len(st)
