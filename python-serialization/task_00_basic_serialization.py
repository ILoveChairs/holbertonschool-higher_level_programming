#!/usr/bin/python3

'''
    quick doc
'''

import pickle


def serialize_and_save_to_file(data, filename):
    '''
        quick doc
    '''

    output = pickle.dumps(data)

    with open(filename, "w+") as f:
        f.write(output)


def load_and_deserialize(filename):
    '''
        quick doc
    '''

    data = None

    with open(filename, "r") as f:
        data = f

    return pickle.loads(data)
