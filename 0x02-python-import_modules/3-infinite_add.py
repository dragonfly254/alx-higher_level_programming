#!/usr/bin/python3
def add_inf(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    sum = 0
    i = 1
    while i <= n:
        sum += int(argv[i])
        i += 1
    print("{:d}".format(sum))


if __name__ == "__main__":
    import sys
    add_inf(sys.argv)
