#Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.

#!/usr/bin/python

def is_palindrome(st):
    regex = [',', '.', '?', ' ', '\'', '!']
    st_lst = []

    for i in st:
        if i not in regex:
            st_lst.append(i.lower())

    if st_lst == st_lst[::-1]:
        return True
    else:
        return False

print is_palindrome(raw_input('Enter a phrase: '))
