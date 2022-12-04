#!/usr/bin/python3
import hidden_4
def alphabet():
    words = dir(hidden_4)
    for i in words:
        if i[:2] != "__":
            print(i)
if __name__ == "__main__":
    alphabet()
