#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description
with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON
    serialization of an object.
    Args:
        obj: The object to be serialized.
    Returns:
        A dictionary representation of the object suitable for JSON
        serialization.
    """
    return obj.__dict__
