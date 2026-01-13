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
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print("{}".format(i), end="")
