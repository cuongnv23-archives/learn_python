#!/usr/bin/env python
#
# name: ex10.py
#

"""
10. Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise,
you should (also) write it using two nested for-loops.
"""

from ex9 import is_member

def overlapping(a, b):
    result = False
    for x in a:
        if is_member(x, b):
            result = True
            break
    return result

if __name__ == '__main__':
    a = ('1', 5, 6, 'asdgasdgasdg', 'sa')
    b = ('1z', 5, 6, 'asdfasdgasdgasdg', 'zz','asdg')
    print '[+] Array 1: ', a
    print '[+] Array 2: ', b
    print overlapping(a, b)