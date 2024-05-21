#!/usr/bin/python3

'''
    Duck
'''


def print_square(size):
    '''
        Goes quack quack
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for element in range(size):
            print("#", end="")
        print("")
