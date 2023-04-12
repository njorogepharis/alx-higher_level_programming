#!/usr/bin/python3
import json
"""loads an object from the json file"""


def load_from_json_file(filename):
    """load object"""
    with open(filename, mode='r', encoding='utf-8') as f:
        return(json.load(f))
