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

    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{key}'")
        self.__dict__['first_name'] = value

    def __getattr__(self, key: str) -> Any:
        if not (key == 'first_name' or '__dict__'):
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{key}'")
        return self.__dict__['first_name']
