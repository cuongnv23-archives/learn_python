#!/usr/bin/env python
#
# name: ex14.py
#

"""
The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three
numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many
 they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.
"""

from sys import argv

def max_in_list(l):
    if type(l) == tuple or type(l) == list:
        try:
            i = [int(i) for i in l]
        except ValueError as msg:
            return '[!] Error, %s ' %msg
        max = l[0]
        for i in l[1:]:
            if i > max:
                max = i
        return max
    else:
        return "[!] Error, " + l + " is not a \"list\" or a \"tupple\""
if __name__ == '__main__':
    if len(argv) <= 2:
        print "[!] Usage: %s element1 element2 [elements..]" %argv[0]
        exit(1)
    list_test = []
    for e in argv[1:]:
        list_test.append(e)
    print max_in_list(list_test)