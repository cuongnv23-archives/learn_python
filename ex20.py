#!/usr/bin/env python
#
# name: ex20.py
#

"""
Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"ar"}
and use it to translate your Christmas cards from English into Swedish. That is, write a function translate()
that takes a list of English words and returns a list of Swedish words.
"""

dic = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
def translate(s):
    split_s = str(s).split()
    result = ""
    for w in split_s:
        result += dic[w] + ' '
    return result

if __name__ == '__main__':
    trans_check = raw_input('[+] Test string: ')
    print translate(trans_check)