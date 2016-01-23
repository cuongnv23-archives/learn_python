#!/usr/bin/env python
#
# name: ex9.py
#

"""
9. Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a,
and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does,
but for the sake of the exercise you should pretend Python did not have this operator.)
"""

def is_member(x, a):
    result = False
    for i in a:
        if str(x) == str(i):
            result = True
            break
    return result

if __name__ == '__main__':
    c = raw_input('[+] Check element: ')
    a = ('1', 2, 3, 'asdgasdgasdg','sa')
    print '[!] Checked array: ', a
    print '[!] Result: ', is_member(c, a)

