#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argv = sys.argv
n = len(argv) - 1
i = 1
sum = 0
while i < len(argv):
    sum += int(argv[i])
    i += 1
print("{:d}".format(sum))
