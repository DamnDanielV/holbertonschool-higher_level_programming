#!/usr/bin/python3


class Square:
    """se inicializan los atributos con __init"""
    def __init__(self, size):
        """tres tipos de atributos:
        privados: self.__priv
        protegidos: self._prot
        publicos: self.publ
        """
        """este ejercicio requiere un atributo privado de objeto"""
        self.__size = size
