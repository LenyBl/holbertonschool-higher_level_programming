#!/usr/bin/python3
"""
This module defines a Square class with a size attribute.
"""


class Square:
    """Represents a square.

    This class stores the size of the square in a private attribute.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initialize a Square instance with a given size.
        Args:
            size (int): The size of the square (default is 0).
        """
        self.size = size
