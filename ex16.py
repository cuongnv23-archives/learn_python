#!/usr/bin/python
#Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

def filter_long_words(st, n):
    st = st.split()
    longer = []
    for i in st:
        if len(i) > int(n):
            longer.append(i)

    return longer

s = raw_input('Enter list of words: ')
num = raw_input('Enter a number: ')

print "Words in which longer than %d: %s" % ( int(num), filter_long_words(s, int(num)) )
