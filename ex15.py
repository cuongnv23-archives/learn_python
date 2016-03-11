#Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

#!/usr/bin/python

def find_longest_word(st):
    st = st.split()
    w = st[0]
    longest = len(w)
    for s in st:
        if len(s) > longest:
            longest = len(s)
            w = s

    return w, longest

st1 = raw_input('Enter list of words: ')
print "Longest word:", find_longest_word(st1)
