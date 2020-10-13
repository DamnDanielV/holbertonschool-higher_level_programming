"""Module Rectangle"""
from models.base import Base
import sys


class Rectangle(Base):
    """class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init variables of objets of class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def height(self):
        """returns de height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height value"""
        if not isinstance(value, (int, bool, float)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """gets width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value"""
        if not isinstance(value, (int, bool, float)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """return the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method that returns the area"""
        return self.__height * self.__width

    def display(self):
        """method  to print the rectangule in #"""
        print("\n" * self.__y, end="")

        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """method str to print"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """method to read args values"""

        arguments = list(args)
        try:
            if len(arguments) > 0:
                self.id = arguments[0]
                self.width = arguments[1]
                self.height = arguments[2]
                self.x = arguments[3]
                self.y = arguments[4]
            else:
                for key in kwargs.keys():
                    setattr(self, key, kwargs[key])
        except IndexError:
            pass

    def to_dictionary(self):
        """returns a dictyonary representation"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
