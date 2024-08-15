#!/usr/bin/python3

'''
    Quickdoc
'''


class MetaClass:
    ''' quickdoc '''

    def __setattr__(self, key, value):
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{key}'")


class LockedClass(MetaClass):
    ''' quickdoc '''

    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{key}'")
        self.__dict__['first_name'] = value
