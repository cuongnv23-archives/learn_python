#
#Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. #For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
#
# Sample input:
# $ python ex6.py
# Enter number(s) separated by a space: 1 2 3
# Sum: 6
# Multiple: 6
#

#!/usr/bin/python

## convert elements to integer
def int_list(a):
    a_list = a.split(' ')
    a_list = [ int(x) for x in a_list]
    return a_list

def a_sum(a):
    a_list = int_list(a)
    s = 0
    for i in a_list:
        s = s + i
    return s

def a_multi(a):
    a_list = int_list(a)
    s = 1
    for i in a_list:
        s = s * i
    return s

a = raw_input('Enter number(s) separated by a space: ')
print "Sum:", a_sum(a)
print "Multiple:", a_multi(a)
