#!/usr/bin/env python
#
# name: ex11.py
#
"""
11. Define a function generate_n_chars() that takes an integer n and a character c and returns a string,
 n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx".
 (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx".
 For the sake of the exercise you should ignore that the problem can be solved in this manner.)
"""

from sys import argv

def generate_n_chars(n, c):
    try:
        n = int(n)
        c = str(c)
    except ValueError as msg:
        print '\n[!] Oops, %s' %(msg)
        return ''

    if len(c) != 1:
        print '\n[!] Oops, invalid input. Character only.'
        print 'Usage: generate_n_chars(number_of_chacraters, character)'
        return ''

    if n < 1:
        print '\n[!] Oops, invalid input. Number_of_characters must be greater than 1.'
        print 'Usage: generate_n_chars(number_of_chacraters, character)'
        return ''
    else:
        result = ''
        for i in range(0,n):
            result += c
        return result


if __name__ == '__main__':
    script, num, char =  argv
    print '[+] The result: ', generate_n_chars(num, char)
