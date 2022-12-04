#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = -len(my_list)
    p = len(my_list) - 1
    i = 0
    while i < len(my_list) and p >= 0:
        i = p + n
        print("{:d}".format(my_list[i]))
        p -= 1
        i += 1
if __name__ == "__main__":
    print_reversed_list_integer
