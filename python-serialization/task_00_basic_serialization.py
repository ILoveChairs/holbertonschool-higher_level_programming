#!/usr/bin/python3

'''
    quick doc
'''

import json


def serialize_and_save_to_file(data, filename):
    '''
        quick doc
    '''

    with open(filename, "w+") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    '''
        quick doc
    '''

    read = None
    with open(filename, "r") as f:
        read = json.load(f)
    return read
