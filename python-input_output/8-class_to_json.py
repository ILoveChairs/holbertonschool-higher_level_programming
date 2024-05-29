#!/usr/bin/python3

'''
    quick doc
'''


def class_to_json(obj):
    '''
        quick doc
    '''

    return { x for x in dir(obj) if x[:2] != "__"}
