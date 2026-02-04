#!/usr/bin/python3
"""
Module defining an abstract base class Animals
with an abstract method sound.
"""

from abc import ABC, abstractmethod


class Animals(ABC):
    """Abstract base class for animals with an abstract method sound."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animals):
    """Dog class that inherits from Animals and implements sound."""

    def sound(self):
        """Return the sound made by the dog."""
        return "Bark"


class Cat(Animals):
    """Cat class that inherits from Animals and implements sound."""

    def sound(self):
        """Return the sound made by the cat."""
        return "Meow"
