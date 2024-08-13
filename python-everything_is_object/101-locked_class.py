#!/usr/bin/python3

'''
    Quickdoc
'''



class LockedClass():
    ''' quickdoc '''

    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
        object.__setattr__(self, key, value)
