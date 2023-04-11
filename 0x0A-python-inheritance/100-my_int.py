#!/usr/bin/python3
""" create myInt class"""


class MyInt(int):
    """define instance of MyInt"""

    def __init__(self, value):
        """initializes the class"""
        self.value = value

    def __eq__(self, b):
        """reverse the = to !="""
        return self.value != b

    def __ne__(self, b):
        """reverses  != to ="""
        return self.value == b
