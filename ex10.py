#!/usr/bin/python

#Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.

from sys import exit

def overlapping(st1, st2):
    n = 0
    new_st1 = st1.split(' ')
    new_st2 = st2.split(' ')

    for x in new_st1:
        for y in new_st2:
            if y == x:
                print True
                exit(0)
            else:
                n = n + 1

    if n != 0:
        print False

s1 = raw_input('Enter 1st list separated by a space: ')
s2 = raw_input('Enter 2dn list separated by a space: ')

overlapping(s1, s2)
