#!/usr/bin/python3
"""module of a class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry without area"""
    def area(self):
        """public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates a value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class rectangle that inherets from BaseGeometry"""
    def __init__(self, width, height):
        """initializes a new object of class Rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method to calculates area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """return an specification of rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """iniatilizes a object class Rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
