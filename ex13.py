#!/usr/bin/python
#The function max() from exercise 1) and the function max_of_three() from exercise 2)
#will only work for two and three numbers, respectively.
#But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are?
#Write a function max_in_list() that takes a list of numbers and returns the largest one.

def max_in_list(l):
    l = l.split(' ')
    arr = [ int(x) for x in l ]
    max = arr[0]
    i = 0
    while i < len(arr):
        if arr[i] > max:
            max = arr[i]
        i = i + 1
    return max

inp = raw_input('Enter list of number: ')
print "Max: ",max_in_list(inp)
