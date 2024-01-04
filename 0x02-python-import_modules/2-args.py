#!/usr/bin/python3
import sys


def main():
    len_arg = len(sys.argv) - 1
    if len_arg == 0:
        print("0 arguments.")
        return

    elif len_arg == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len_arg))

    for i, arg in enumerate(sys.argv[1:]):
        print("{:d}: {}".format(i + 1, arg))


if __name__ == "__main__":
    main()
