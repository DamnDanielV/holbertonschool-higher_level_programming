#!/usr/bin/python3


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """instantiation attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict reperesntation of a class"""
        if attrs is None:
            my_dict = self.__dict__
            return my_dict
        else:
            my_dict = self.__dict__
            return dict(([key, value] for key,
                        value in my_dict.items() if key in attrs))

    def reload_from_json(self, json):
        """replaces all attributes"""
        for key, value in json.items():
            setattr(self, key, value)
