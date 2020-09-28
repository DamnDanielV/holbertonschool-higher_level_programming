#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation of width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method to returns area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """method to returns perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """prints a square of #"""
        st_re = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            for char in range(self.__height):
                st_re += str(self.print_symbol * self.__width) + "\n"
            return st_re

    def __repr__(self):
        """returns strings representation of aquare"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(Self):
        """detects of a deletion instance"""
        Rectangle.number_of_instances -= 1
        return (print("Bye rectangle..."))

    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """return a new rectangle instance with width == height == size"""
        return Rectangle(size, size)
