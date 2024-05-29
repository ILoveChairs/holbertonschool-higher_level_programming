#!/usr/bin/python3

'''
    quick doc
'''

from io import StringIO
import json


def from_json_string(my_str):
    '''
        quick doc
    '''

    io = StringIO(my_str)
    return json.load(io)
