#!/usr/bin/python3

for num in range(0, 100):
    if num == 99:
        print("{:n}".format(num))
    else:
        print("{:n}, ".format(num), end="")
