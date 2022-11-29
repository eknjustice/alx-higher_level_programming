#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
zero = "and is 0"
greaterThan5 = "and is greater than 5"
lessThan6 = "and is less than 6 and not 0"
if number < 0:
    last_digit = -((-number) % 10)
    print(f"Last digit of {number:d} is {last_digit} {lessThan6}")
else:
    last_digit = number % 10
    if last_digit > 5:
        print(f"Last digit of {number:d} is {last_digit} {greaterThan5}")
    elif last_digit == 0:
        print(f"Last digit of {number:d} is {last_digit} {zero}")
    else:
        print(f"Last digit of {number:d} is {last_digit} {lessThan6}")
