#!/usr/bin/python
#Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)

from sys import exit

def is_member(list, element):
    i = 0
    match_counts = 0
    list = list.split(' ') # convert input to list with separator is a space
    
    while i < len(list):
        if list[i] == element:
            match_counts = 0
            print True
            exit(0)
        else:
            i += 1
            match_counts += 1

    if match_counts != 0:
        print False

x = raw_input('Enter a list3: ')
a = raw_input('Enter a value: ')
is_member(x, a)
