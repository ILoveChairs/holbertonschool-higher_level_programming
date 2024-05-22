#!/usr/bin/python3

'''
    DGQQ
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
        Perfect rectangle
    '''

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
