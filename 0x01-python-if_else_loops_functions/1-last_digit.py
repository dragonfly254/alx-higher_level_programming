#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# handling negative number
flag = 0
if number < 0:
    number *= -1
    flag = 1

# calculating last digit
last_d = number % 10

# last digit for negative number
if flag:
    number *= -1
    last_d *= -1

if last_d > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
elif last_d == 0:
    print(f"Last digit of {number} is {last_d} and is 0")
else:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")
