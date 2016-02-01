#Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner.)

#!/usr/bin/python

def generate_n_chars(n, c):
    i = 0
    s = []
    while i < n:
        s.append(c)
        i = i + 1

    result = ''.join(s)
    return result

num = raw_input('Enter number of character to generate: ')
char = raw_input('Enter a character: ')
s = generate_n_chars(int(num), char)
print "Generated string: ", s
