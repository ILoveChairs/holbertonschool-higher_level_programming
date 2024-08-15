#!/usr/bin/python3

'''
    Quickdoc
'''


class MetaClass(type):
    ''' quickdoc '''

    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError(
                f"'LockedClass' object has no attribute '{key}'")
        self.__dict__['first_name'] = value


class LockedClass(MetaClass, metaclass=MetaClass):
    ''' quickdoc '''

    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{key}'")
        self.__dict__['first_name'] = value
