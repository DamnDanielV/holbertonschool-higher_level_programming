#!/usr/bin/python3
"""module class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """classe Square inherits from Recatngle"""
    def __init__(self, size, x=0, y=0, id=None):
        """init a object class Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method str"""
        return "[Square] {} {}/{} - {}".format(self.id, self.x,
                                               self.y, self.height)

    @property
    def size(self):
        """get size square"""
        return self.height

    @size.setter
    def size(self, value):
        """sets the vaue of size"""
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """method to update attributes"""
        arguments = list(args)

        try:
            if len(arguments) > 0:
                self.id = arguments[0]
                self.size = arguments[1]
                self.x = arguments[2]
                self.y = arguments[3]
            else:
                for key in kwargs.keys():
                    setattr(self, key, kwargs[key])
        except IndexError:
            pass

    def to_dictionary(self):
        """returns a dictyonary representation"""
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
