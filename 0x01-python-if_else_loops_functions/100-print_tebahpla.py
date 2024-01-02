#!/usr/bin/python3
flag = 1
for c in range(122, 96, -1):
    if flag % 2 == 0:
        c -= 32
    print("{:s}".format(chr(c)), end="")
    flag += 1
