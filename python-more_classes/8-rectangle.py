#!/usr/bin/python3

'''
    Defines rectangle class.
'''


class Rectangle:
    '''
        Rectangle class.

        number_of_instances(int): Number of instances.
        height(int, >=0): Height of rectangle.
        width(int, >=0): Width of rectangle.
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __str__(self):
        output = ""
        if self.width == 0 or self.height == 0:
            return ""
        for x in range(self.height):
            line = ""
            for y in range(self.width):
                line += str(self.print_symbol)
            output += f"{line}\n"
        return output[:-1]

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
