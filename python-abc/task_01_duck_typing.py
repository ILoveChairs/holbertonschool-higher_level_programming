#!/usr/bin/python3

'''
    Using ABC
'''

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    '''
        Shape
    '''

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    '''
        Circle

        private radius(int): Radius of circle, >= 0
    '''

    def __init__(self, radius):
        if not isinstance(radius, int):
            raise TypeError("radius must be an int")
        if radius < 0:
            raise ValueError("radius must be >= 0")
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * pi

    def perimeter(self):
        return self.__radius * pi * 2


class Rectangle(Shape):
    '''
        Rectangle

        private width(int): Width of rectangle, >= 0
        private height(int): Height of rectangle, >= 0
    '''

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return max(self.__height * self.__width, 0)

    def perimeter(self):
        return max(self.__height * 2 + self.__width * 2, 0)


def shape_info(shape: Shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
