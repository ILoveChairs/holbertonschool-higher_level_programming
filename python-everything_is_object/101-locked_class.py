#!/usr/bin/python3

'''
    Quickdoc
'''



class LockedClass():
    ''' quickdoc '''

    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError(
                f"'LockedClass' object has no attribute '{key}'")
        object.__setattr__(self, key, value)
