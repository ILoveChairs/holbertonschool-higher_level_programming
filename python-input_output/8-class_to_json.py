#!/usr/bin/python3

'''
    quick doc
'''

import json


def class_to_json(obj):
    '''
        quick doc
    '''

    return json.dumps(obj, default=lambda o: o.__dict__)
