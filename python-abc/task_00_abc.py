#!/usr/bin/python3

from abc import ABC, abstractmethod
"""
Module defining an abstract base class Animals
with an abstract method sound.
"""


class Animals(ABC):
    """ Abstract base class for animals with an abstract method sound."""
    @abstractmethod
    def sound(self):
        """ Abstract method to be implemented by subclasses to produce
        animal sound."""
        pass


class Dog(Animals):
    """ Dog class that inherits from Animals and implements the sound
    method."""
    def sound(self):
        """
        Returns the sound made by the dog.
        """
        return "Bark"


class Cat(Animals):
    """ Cat class that inherits from Animals and implements the sound
    method."""
    def sound(self):
        """
        Returns the sound made by the cat.
        """
        return "Meow"
