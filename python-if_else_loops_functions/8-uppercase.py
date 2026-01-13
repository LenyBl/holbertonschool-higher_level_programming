#!/usr/bin/python3
def uppercase(c):
    """Convert a lowercase character to uppercase.

    Args:
        c (str): A single character string.
    Returns:
        str: The uppercase equivalent if c is lowercase, else returns c unchanged.
    """
    for i in (c):
        if 97 <= ord(i) <= 122:
            return chr(ord(i) - 32)
        else:
            return i
