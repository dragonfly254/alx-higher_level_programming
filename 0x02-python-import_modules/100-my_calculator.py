#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

def main():
    args = sys.argv
    if len(args) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(args[1])
    b = int(args[3])
    op = args[2] 

    ops = {
            "+" : add,
            "-" : sub,
            "*" : mul,
            "/" : div
            }

    if op in ops.keys():
        print("{:d} {} {:d} = {:d}".format(a, op, b, ops[op](a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
