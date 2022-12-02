#!/usr/bin/python3
def arguments():
    words = input()
    i = 0
    argv = words.split()
    argc = len(argv)
    if argc == 0 and words == "enter":
        print(argc, "arguments:")
    else:
        if argc == 1:
            print(argc, "argument:")
            print("{:d}".format(argc), argv[argc])
        else:
            print(argc, "arguments:")
            for i in range(argc):
                print(i, argv[i])

arguments()
