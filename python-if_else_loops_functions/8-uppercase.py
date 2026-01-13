#!/usr/bin/python3
def uppercase(c):
    """Convert a lowercase character to uppercase.

    Args:
        c (str): A single character string.
    Returns:
        str: The uppercase equivalent if c is lowercase, else returns c unchanged.
    """
    if 'a' <= c <= 'z':
        print("{}".format(chr(ord(c) - 32)))
    else:
        print("{}".format(c))
