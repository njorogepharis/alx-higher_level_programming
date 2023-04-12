#!/usr/bin/python3
"""reads the file"""


def read_file(filename=""):
    """reads the file"""
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
