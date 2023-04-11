#!/usr/bin/python3
"""Base geometry class"""


class BaseGeometry:

    def area(self):
        """raises the exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value for the integer and the positive"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""class : rectangle"""


class Rectangle(BaseGeometry):
    """creates the rectangle class"""
    def __init__(self, width, height):
        """initializes the given rectangle"""
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height
