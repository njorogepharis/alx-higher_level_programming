#!/usr/bin/python3
"""student class"""


class Student:
    """class items"""
    def __init__(self, first_name, last_name, age):
        """initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """print the __dict__"""
        return self.__dict__
