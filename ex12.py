#Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

#****
#*********
#*******

#!/usr/bin/python

def histogram(s):
    s = s.split(' ')
    s = [ int(a) for a in s ] # convert string to integer
    for i in s:
        x = 0
        b = []
        while x < i:
            b.append("*")
            x = x + 1
        print ''.join(b)

l = raw_input('Enter list of numbers: ')
histogram(l)
