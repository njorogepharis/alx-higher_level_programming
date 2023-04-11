#!/usr/bin/python3

"""Defines the base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent the base geometry."""

    def area(self):
        """Not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
