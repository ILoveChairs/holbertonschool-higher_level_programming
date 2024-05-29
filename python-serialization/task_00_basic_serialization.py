#!/usr/bin/python3

'''
    quick doc
'''

import pickle


def serialize_and_save_to_file(data, filename):
    '''
        quick doc
    '''

    with open(filename, "wb+") as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    '''
        quick doc
    '''

    read = None
    with open(filename, "rb") as f:
        read = pickle.load(f)
    return read
