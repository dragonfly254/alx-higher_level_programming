#!/usr/bin/python3
def add_inf(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    sum = 0
    for i in range(1, n + 1):
        sum += int(argv[i])
    print("{:d}".format(sum))


if __name__ = "__main__":
    import sys
    add_inf(sys.argv)
