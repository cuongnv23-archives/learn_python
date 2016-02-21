#!/usr/bin/env python
#
# name: ex14.py
#

"""
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
"""

def words_mapping(list_of_words):
    list_of_words = str(list_of_words)
    check_array = list_of_words.split()
    result_list = []
    for w in check_array:
        result_list.append(len(w))
    return result_list
if __name__ == '__main__':
    check_list = "   #^%$$ Qalksdjlkajsdf sdgadsg 2r5   "
    print words_mapping(check_list)
