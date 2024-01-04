#!/usr/bin/python3
import sys


def infinite_add():
    infinite_sum = 0
    
    for i in sys.argv[1:]:
        infinite_sum += int(i)

    print("{:d}".format(infinite_sum))


if __name__ == "__main__":
    infinite_add()
