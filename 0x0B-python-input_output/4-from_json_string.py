#!/usr/bin/python3
"""turns the string to object"""
import json


def from_json_string(my_str):
    """returns the new object"""
    return json.loads(my_str)
