#!/usr/bin/python3
"""student class"""


class Student:
    """class items"""
    def __init__(self, first_name, last_name, age):
        """initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """print the __dict__"""
        if(isinstance(attrs, list) and all(isinstance(x, str) for x in attrs)):
            return({x: y for x, y in self.__dict__.items() if x in attrs})
        else:
            return self.__dict__
