#!/usr/bin/python3
"""save the object as json string dump"""
import json


def save_to_json_file(my_obj, filename):
    """save object"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
