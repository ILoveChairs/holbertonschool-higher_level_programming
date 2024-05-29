#!/usr/bin/python3

'''
    quick doc
'''

import json
from io import StringIO


def load_from_json_file(filename):
    '''
        quick doc
    '''

    io = None
    with open(filename) as f:
        io = StringIO(f)
    return json.load()
