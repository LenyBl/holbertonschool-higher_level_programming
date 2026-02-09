#!/usr/bin/python3
"""
Module file that contains the function append_write
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns the number of
    characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
