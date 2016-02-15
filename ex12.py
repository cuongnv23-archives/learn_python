#!/usr/bin/env python
#
# name: ex12.py
#

"""
12. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
****
*********
*******

"""

from ex11 import generate_n_chars
from sys import argv

def histogram(array):
    for n in array:
        print generate_n_chars(n, '*')
if __name__ == '__main__':
    a = []
    for e in argv[1:]:
        try:
            e = int(e)
            a.append(e)
        except ValueError as msg:
            print '[!] Error, %s.' %msg
    print '[+] Histogram: '
    histogram(a)

