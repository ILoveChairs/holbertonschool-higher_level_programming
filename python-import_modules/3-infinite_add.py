#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv
    result = 0
    for arg in argv[1:]:
        result += int(arg)
    print(result)
