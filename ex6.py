#!/usr/bin/python
#
# name: ex6.py
#
"""
6. Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers.
For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
"""

from sys import argv
def int_check(a):
    try:
        a = [int(i) for i in a]
        return True
    except:
        return  False

def sum(a):
    sum = int(a[0])
    for x in a[1:]:
        sum += int(x)
    return sum

def multiplies(a):
    multi = int(a[0])
    for x in a[1:]:
        multi *= int(x)
    return multi

def help():
    print "[!] Opps, error.\nUsage: %s <integer1> [integer2] [integer3] ..." %(argv[0])

if __name__ == "__main__":
    if len(argv) == 1:
        help()
    else:
        if int_check(argv[1:]):
            print "[+] Sum checking: ", sum(argv[1:])
            print "[+] Multiplies checking: ", multiplies(argv[1:])
        else:
            print "[!] Error, arguments must be all integer."

