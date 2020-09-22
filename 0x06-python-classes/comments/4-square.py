#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")

    def area(self):
        ar = self.__size ** 2
        return ar

    @property   #se invoca la funcion integrada property()
    def size(self): #se define el metodo para obtener el atributo solicitado
        return self.__size  #se retorna dicho atributo privado
    @size.setter    #propiedad setter para modificar un atributo
    def size(self, value):  #se vuelve a definir el atributo con su nuevo valor (value)
        if type(value) != int:  #se realiza el mismo procedimiento que en el __init__ pero con value
            raise TypeError("size must be an integer")
        else:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")