#!/usr/bin/python3
""" Square Module """


class Square:
    """ This is docstring for Square Class """
    def __init__(self, size=0, position=(0, 0)):
        """ instantiation of square with position & size """
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size >= 0:
                self.__size = size

        self.__position = position

    def area(self):
        """ returns area of a square """
        ar = self.__size ** 2
        return ar

    def my_print(self):
        """ prints a square of '#' """
        if (self.__size == 0):
            print()
        else:
            if not (self.__position):
                for i in range(self.__size):
                    print("#" * self.__size)
            else:
                for i in range(self.__position[1]):
                    print()
                for j in range(self.__size):
                    print(" " * self.__position[0], end="")
                    print("#" * self.__size)

    @property
    def size(self):
        """ size variable of Square class instance """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size variable of Square class instance """
        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")

    @property
    def position(self):
        """ position variable of Square class instance """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets position variable of Square class instance """
        if ((len(value) != 2) or (type(value[0] != int) or
           (type(value[1]) != int)) or value[0] < 0 or value[1] < 0 or
           (type(value) != tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
