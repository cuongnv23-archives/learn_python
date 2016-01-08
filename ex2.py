#
#Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
#
#!/usr/bin/python

from sys import argv

script, num_1, num_2, num_3 = argv

def max_of_three(a, b, c):
    max = a
    if b > max and b > c:
        max = b
    elif b > max and b < c:
        max = c
    elif b < max and max < c:
        max = c
    return max

print "Max of three: ", max_of_three(int(num_1), int(num_2), int(num_3))
