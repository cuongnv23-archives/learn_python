#!/usr/bin/python
#Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"ar"} and use it to translate your Christmas cards from English into Swedish. That is, write a function translate() that takes a list of English words and returns a list of Swedish words.

def translate(s):
    dict = {
        "merry": "god",
        "christmas": "jul",
        "and": "och",
        "happy": "gott",
        "new": "nytt",
        "year": "ar"
    }

    key_list = []
    s = s.split()
    for i in s:
        key_list.append(dict[i])

    return key_list

greeting = 'merry christmas and happy new year'
result = translate(greeting)
print "Translated: ", ' '.join(result)
