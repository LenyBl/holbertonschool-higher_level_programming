#!/usr/bin/python3
"""
Module defining a CountedIterator class that wraps an iterable
and counts the number of iterations.
"""


class CountedIterator:
    """
    An iterator that counts the number of iterations.
    Wraps around any iterable and provides a method to get the count
    of iterations performed.
    """
    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.
        args:
            iterable: An iterable to wrap.
        """
        self._iterable = iter(iterable)
        self._count = 0

    def get_count(self):
        """
        Get the number of iterations performed.
        returns:
            int: The number of iterations.
        """
        return self._count

    def __next__(self):
        """
        Get the next item from the iterable and increment the count.
        returns:
            The next item from the iterable.
        raises:
            StopIteration: When the iterable is exhausted.
        """
        self._count += 1
        return next(self._iterable)

    def __iter__(self):
        """
        Return the iterator object itself.
        returns:
            CountedIterator: The iterator object.
        """
        return self
