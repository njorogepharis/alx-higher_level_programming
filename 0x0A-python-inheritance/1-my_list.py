#!/usr/bin/python3

"""Defines class MyList."""

class MyList(list):
    """Sorted printing for given built-in list class."""

    def print_sorted(self):
        """Print the given list in sorted ascending order."""
        print(sorted(self))
