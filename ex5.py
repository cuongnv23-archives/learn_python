#!/usr/bin/python
#
# name: ex5.py
#
# 5. Write a function translate() that will translate a text into "xxxxxxxx" (Swedish for "robber's language").
# That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")
# should return the string "tothohisos isos fofunon".
#

from ex4 import vowel_check
from sys import argv

def consonant_dup(input_str):
    input_str = str(input_str)
    output_str = ''
    for char in input_str:
        if vowel_check(char):
           output_str += char
        else:
            output_str += 'o' + char + 'o'
    return output_str

if __name__ == '__main__':
    script, input_string = argv
    print "[+] Original: %s - [+] Translated: %s" %(input_string, consonant_dup(input_string))