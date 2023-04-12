#!/usr/bin/python3

"""Defines the file-writing function."""


def write_file(filename="", text=""):
    """Write the string to UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
