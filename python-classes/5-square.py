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
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size <= 0:
            print("")
        for y in range(self.size):
            for x in range(self.size):
                print("#", end="")
            print("")
