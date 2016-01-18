#!/usr/bin/env python
#
# name: ex7.py
"""
Define a function reverse() that computes the reversal of a string.
For example, reverse("I am testing") should return the string "gnitset ma I".
"""


from sys import argv

def reverse(input_string):
    result = ''
    result_len  = len(input_string) - 1
    for i in range(0, result_len + 1):
        result += input_string[result_len - i]
    return result


if __name__ == '__main__':
    try:
        script, input_string = argv
        print '[+] Input: ', input_string
        print '[+] Reverse: ', reverse(input_string)
    except ValueError as msg:
        print '[!] Oops, error: %s' %msg


