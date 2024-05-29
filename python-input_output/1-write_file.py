#!/usr/bin/python3

'''
    quick doc
'''


def write_file(filename="", text=""):
    '''
        quick doc
    '''

    n_written = 0
    with open(filename, "w+") as f:
        n_written = f.write(text)
    return n_written
