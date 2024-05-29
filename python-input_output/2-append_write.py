#!/usr/bin/python3

'''
    quick doc
'''

def append_write(filename="", text=""):
    '''
        quick doc
    '''

    n_written = 0
    with open(filename, "a+") as f:
        n_written = f.write(text)
    return n_written
