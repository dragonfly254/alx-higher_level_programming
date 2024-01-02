#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) < 123:
            c = (chr(ord(c) - (ord('a') - ord('A'))))
        print("{:s}".format(c), end="")
    print()
