#Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

#!/usr/bin/python

def find_longest_word(st):
    st = st.split(' ')
    longest = st[0]
    i = 0
    while i < len(st):
        if len(st[i]) > len(longest):
            longest = st[i]
        i = i + 1

    return len(longest)

st1 = raw_input('Enter list of words: ')
print "Longest: ", find_longest_word(st1)
