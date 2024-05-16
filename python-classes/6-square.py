#!/usr/bin/python3

'''Square:
    gil
'''


class Square:
    '''Does square

    Attributes:
        __size (int): Size of square: Param1
        __position (:obj:`tuple` of :obj:`int`): Param2
    '''

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def tuple_error():
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position, tuple):
            tuple_error()
        elif len(position) != 2:
            tuple_error()
        elif position[0] < 0 or position[1] < 0:
            tuple_error()
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        def tuple_error():
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value, tuple):
            tuple_error()
        elif len(value) != 2:
            tuple_error()
        elif value[0] < 0 or value[1] < 0:
            tuple_error()
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size <= 0:
            print("")
        for space in range(self.position[1]):
            print("")
        for y in range(self.size):
            for space in range(self.position[0]):
                print(" ", end="")
            for x in range(self.size):
                print("#", end="")
            print("")
