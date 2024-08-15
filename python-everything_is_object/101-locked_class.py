#!/usr/bin/python3

'''
    Quickdoc
'''


from typing import Any


class MetaClass(type):
    ''' quickdoc '''

    def __setattr__(self, key, value):
        raise AttributeError(
            f"'LockedClass' object has no attribute '{key}'")

    @property
    def __dict__(self):
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '__dict__'")


class LockedClass(metaclass=MetaClass):
    ''' quickdoc '''

    def __init__(self):
        self.____dict__ = {}

    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{key}'")
        self.____dict__['first_name'] = value

    def __getattribute__(self, key: str) -> Any:
        if key != 'first_name':
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{key}'")
        return self.____dict__['first_name']

    @property
    def __dict__(self):
        try:
            return self.____dict__
        except Exception:
            return ''
