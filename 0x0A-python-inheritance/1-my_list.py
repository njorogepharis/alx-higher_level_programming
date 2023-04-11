#!/usr/bin/python3
"""create class mylist"""


class MyList(list):
    """prints the sorted list of class"""
    def print_sorted(self):
        print(sorted(self))
