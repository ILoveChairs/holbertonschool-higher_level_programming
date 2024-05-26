#!/usr/bin/python3

'''
    Adds add_attribute
'''


def add_attribute(cls, varname, value):
    '''
        Adds an attribute safely
    '''
    if not isinstance(cls, object) or not isinstance(varname, str):
        raise TypeError("can't add new attribute")
    if "__setattr__" not in dir(cls):
        raise TypeError("can't add new attribute")
    setattr(cls, varname, value)
