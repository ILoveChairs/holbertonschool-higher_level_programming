#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc > 1:
        print(f"{argc} arguments")
    else:
        print("1 argument")
    for i, arg in enumerate(sys.argv):
        print(f"{i + 1}: {arg}")
