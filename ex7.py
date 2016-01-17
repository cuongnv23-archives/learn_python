#
#Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".
#

#!/usr/bin/python

def reverse(s):
    a_list = []
    b_list = []
    for i in s:
        a_list.append(i)

    while len(a_list) != 0:
        b_list.append(a_list.pop())

    return ''.join(b_list)


a = raw_input("Enter a string to reverse:")
print "Reversed: ", reverse(a)
