#!/usr/bin/python3

'''
    Quickdoc
'''


class LockedClass():
    ''' quickdoc '''

    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{key}'")
        object.__setattr__(self, key, value)
