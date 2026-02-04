#!/usr/bin/python3
"""
Module defining an abstract base class Shape with abstract methods area
and perimeter.
It also includes Circle and Rectangle classes that implement these methods,
and a function shape_info that prints the area and perimeter of a given shape.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for shapes with abstract methods area and perimeter.
    """
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape and implements area and
    perimeter.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return "Area: " + str(3.14159 * (self.radius ** 2))

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return "Perimeter: " + str(2 * 3.14159 * self.radius)


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape and implements area and
    perimeter.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return "Area: " + str(self.width * self.height)

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return "Perimeter: " + str(2 * (self.width + self.height))


def shape_info(shape):
    """Print the area and perimeter of the given shape."""
    print(shape.area())
    print(shape.perimeter())
