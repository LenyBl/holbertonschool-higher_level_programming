#!/usr/bin/python3
"""
This module contains a class for creating custom objects and methods for
serializing and deserializing them using the pickle module.
"""
import pickle


class CustomObject:
    """
    A class representing a custom object with attributes and methods for
    serialization and deserialization.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        import pickle
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
