#!/usr/bin/python3
def print_last_digit(number):
    number_as_string = str(number)
    last_digit_as_string = number_as_string[-1]
    last_digit = int(last_digit_as_string)
    print(last_digit)
