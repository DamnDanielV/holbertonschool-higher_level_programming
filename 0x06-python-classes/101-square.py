#!/usr/bin/python3
""" Square Module """


class Square:
    """ This is a docstring of Square Class """
    def __init__(self, size=0, position=(0, 0)):
        """ instantiation of square with size & position """
        self.size = size
        self.position = position

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
        """ position variable of Square """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets position variable of Square """
        if (len(value) != 2 or type(value[0]) != int or
           type(value[1]) != int or value[0] < 0 or value[1] < 0 or
           type(value) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ area of a square """
        return self.__size**2

    def my_print(self):
        """ square of '#' """
        if self.__size == 0:
            print()
            return
        if (self.__position):
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            for i in range(self.__size):
                print('#' * self.__size)

    def __str__(self):
        """square to strings of #"""
        ch = ""
        if self.__size != 0:
            if not (self.__position):
                for i in range(self.__size):
                    ch += str(("#" * self.__size) + "\n")
                ch = ch[:-1]
            else:
                for i in range(self.__position[1]):
                    ch += "\n"
                for i in range(self.__size):
                    ch += str(" " * self.__position[0])
                    ch += str(("#" * self.__size) + "\n")
                ch = ch[:-1]
        return ch
