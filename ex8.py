#!/usr/bin/python

#Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.

import string

def reverse(s):

    b_list = []
    a_list = conv_2_list(s) # remove all spaces of s and create a list

    while len(a_list) != 0:
        b_list.append(a_list.pop())
    return b_list

def conv_2_list(s):

    a_list = []
    ignores = [',', '.', '?', ' ', '\'', '!']

    for i in s.lower(): #convert all elements to lowercase
        if ( i not in ignores ): #ignore regex
            a_list.append(i)
    return a_list

def is_palindrome(s):
    pal = reverse(s)
    s = conv_2_list(s)

    if pal == s:
        print True
    else:
        print False

a = raw_input('Enter a string: ')
is_palindrome(a)
