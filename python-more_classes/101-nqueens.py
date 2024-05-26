#!/usr/bin/python3

'''
    Usage: nqueens N
'''

from sys import argv


def root(P):
    '''
        quick doc
    '''
    pass


def reject(P, c):
    '''
        quick doc
    '''
    pass


def accept(P, c):
    '''
        quick doc
    '''
    pass


def first(P, c):
    '''
        quick doc
    '''
    pass


def nxt(P, s):
    '''
        quick doc
    '''
    pass


def queenBacktrack(P, c):
    '''
        quick doc
    '''
    if reject(P, c):
        return
    if accept(P, c):
        output(P, c)
    s = first(P, c)
    while s is not None:
        queenBacktrack(P, s)
        s = nxt(P, s)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    N = argv[1]
    if not N.isdigit():
        print("N must be a number")
        exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    queenBacktrack(None, None)
