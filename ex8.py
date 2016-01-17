#Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.

#!/usr/bin/python

def reverse(s):
    a_list = []
    b_list = []
    
    for i in s:
        a_list.append(i)

    while len(a_list) != 0:
        b_list.append(a_list.pop())

    return ''.join(b_list)

def is_palindrome(s):
    new_s = reverse(s)
    if new_s == s:
        print True
    else:
        print False

a = raw_input('Enter a string: ')
is_palindrome(a)
