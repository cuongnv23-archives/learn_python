#!/usr/bin/env python
#
# name: ex21.py
#
"""
Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it.
Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
"""


def char_freq(s):
    rs = {}
    s = s.split()
    for w in s:
        for c in w:
            if c not in rs:
                rs[c] = 1
            else:
                rs[c] += 1
    return rs

if __name__ == '__main__':
    t = raw_input('[+] Testing string: ')
    print '[+] Frequency listing: '
    rs = char_freq(t)
    for i in rs.keys():
        print "- %s: %d" %(i,rs[i])
