#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberString = str(number)
last_digit = int(numberString[-1])
if number >= 0:
    if  last_digit > 5:
        new = "and is greater than 5"
    elif last_digit < 6 and last_digit != 0:
        new = "and is less than 6 and not 0"
    else:
        new = "and is zero"
    print(f"Last digit of {number:d} is {last_digit} {new}")
elif number < 0:
    if last_digit == 0:
        print(f"Last digit of {number:d} is {last_digit} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number:d} is -{last_digit} and is less than 6 and not 0")
