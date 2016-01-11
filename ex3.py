###
#Define a function that computes the length of a given list or string.
#(It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
#

#!/usr/bin/python

def len_str(s):
    len = 0
    for i in s:
        len = len + 1
    return len

str = raw_input('Enter your string:')

print "Length of string is: ", len_str(str)
