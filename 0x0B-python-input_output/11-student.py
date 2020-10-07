#!/usr/bin/python3


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """instantiation attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict reperesntation of a class"""
        my_dict = self.__dict__

        return my_dict
