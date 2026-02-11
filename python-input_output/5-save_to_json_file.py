#!/usr/bin/python3
"""
Module file that contains the function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation
    """
    object_to_string = json.dumps(my_obj)
    json_text = json.loads(object_to_string)
    with open(filename, "w") as f:
        f.write(str(json_text))
