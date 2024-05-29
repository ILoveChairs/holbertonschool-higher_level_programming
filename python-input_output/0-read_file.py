#!/usr/bin/python3

'''
	quick doc
'''


def read_file(filename=""):
    '''
        quick doc
    '''

    with open(filename) as f:
        for line in f:
            print(line, end="")
