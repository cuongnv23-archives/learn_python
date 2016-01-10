#!/usr/bin/env python
#
"""
2. Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
"""

# Find out the maximum number from an array, used for integer only
def max_of_number(a):
    # Assign the first number is the maximum
    try:
        max = int(a[0])
    except ValueError as msg:
        print("[!] Oops, invalid number input. \n\
Message: %s" %(msg))
        exit()
    # Checking for ther others
    for num in a[1:]:
        try:
            num = int(num)
        except ValueError as msg:
            print("[!] Oops, invalid number input. \n\
Message: %s" %(msg))
            exit()
        if num > max:
            max = num
    return max

# The main function
if __name__ == "__main__":
    checkArray = []
    x = raw_input("[+] The first number: ")
    y = raw_input("[+] The second number: ")
    z = raw_input("[+] The third number: ")
    checkArray.append(x)
    checkArray.append(y)
    checkArray.append(z)
    maxNum = max_of_number(checkArray)
    print("[!] The maximum number: %d" %(maxNum))