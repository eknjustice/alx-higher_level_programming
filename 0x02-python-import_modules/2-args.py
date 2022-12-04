#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argv = sys.argv
n = len(argv) - 1
i = 1
if n == 0:
    print("{:d} argument.".format(n))
else:
    if n == 1:
        print("{:d} argument:".format(n))
        print("{:d}: {:s}".format(i, argv[i]))
    else:
        print("{:d} arguments:".format(n))
        while i <= n:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
