#!/usr/bin/python3
"""basegeometryclass"""


class BaseGeometry:

    def area(self):
        """raises given exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the given value for the integer and positive"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""class rectangle"""


class Rectangle(BaseGeometry):
    """creates  a rectangle class"""
    def __init__(self, width, height):
        """initializes the rectangle"""
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height

    def area(self):
        """return the area"""
        return self.__width * self.__height

    def __str__(self):
        """return thestring"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
