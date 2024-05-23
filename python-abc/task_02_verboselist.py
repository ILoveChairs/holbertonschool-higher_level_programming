#!/usr/bin/python3

'''
    Making our own list from list
'''

from typing import Iterable, SupportsIndex


class VerboseList(list):
    '''
        VerboseList <- list
    '''

    def append(self, __object) -> None:
        result = super().append(__object)
        print(f"Added [{__object}] to the list.")
        return result

    def extend(self, __iterable: Iterable) -> None:
        result = super().extend(__iterable)
        print(f"Extended the list with [{len(__iterable)}] items")
        return result

    def remove(self, __value) -> None:
        print(f"Removed [{__value}] from the list")
        return super().remove(__value)
    def pop(self, __index: SupportsIndex = -1):
        print(f"Popped [{self.__getitem__(__index)}] from the list.")
        return super().pop(__index)
