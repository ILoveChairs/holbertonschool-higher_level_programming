#!/usr/bin/python3

'''
    DGQQ
'''


def inherits_from(obj, a_class):
    '''
        Duck Goes Quack Quack
    '''
    return a_class in obj.__class__.__mro__ and not \
        obj.__class__.__name__ == a_class.__name__
