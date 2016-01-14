#Write a function translate() that will translate a text into "" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".
#
# Sample input:
# $ python ex5.py
# Enter a string:learn python the hard way
# lolearornon popyoytothohonon tothohe hoharordod wowayoy


#!/usr/bin/python

def translate(s):
    trans = []
    for i in s:
        if i not in "a u e i o":
            a = i + "o" + i
        else:
            a = i
        trans.append(a)
    result = ''.join(trans) # this is not a magic
    return result

a = raw_input('Enter a string: ')
print "Translated: ", translate(a)
