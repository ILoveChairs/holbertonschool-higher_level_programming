#!/usr/bin/python3
'''
    DGQQ
'''


def is_kind_of_class(obj, a_class):
    '''
        Duck Goes Quack Quack
    '''
    return a_class in obj.__class__.__mro__ or \
        obj.__class__.__name__ == a_class.__name__
