#!/usr/bin/python3

'''Square:
    gil
'''


class Square:
    '''Does square

    Attributes:
        __size (int): Size of square
    '''

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    @property
    def area(self):
        return self.__size ** 2
