#!/usr/bin/python3
"""the subclass checker"""


def inherits_from(obj, a_class):
    """returns the subclass yes"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
