#!/usr/bin/python3

'''
    quick doc
'''

import json


def save_to_json_file(my_obj, filename):
    '''
        quick doc
    '''

    with open(filename, "w+") as f:
        f.write(json.dumps(my_obj))
