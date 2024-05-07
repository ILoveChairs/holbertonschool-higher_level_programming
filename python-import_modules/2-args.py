#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if argc > 1:
        print(f"{argc} arguments:")
    elif argc == 1:
        print("1 argument:")
    else:
        print("0 arguments.")
    for i, arg in enumerate(sys.argv[1:]):
        print(f"{i + 1}: {arg}")
