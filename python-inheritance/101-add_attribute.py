#!/usr/bin/python3

'''
    Adds add_attribute
'''


def add_attribute(cls, varname, value):
    '''
        Adds an attribute safely
    '''
    d = dir(cls)
    if not isinstance(varname, str):
        raise TypeError("can't add new attribute")
    if "__dict__" not in d:
        raise TypeError("can't add new attribute")
    if "__setattr__" not in d:
        raise TypeError("can't add new attribute")
    setattr(cls, varname, value)
