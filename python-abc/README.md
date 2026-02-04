
# Abstract Classes in Python

## Overview
Abstract classes are classes that cannot be instantiated directly. They serve as blueprints for other classes and enforce a contract that subclasses must follow.

## Key Concepts

**Abstract Base Class (ABC)**
- Use the `abc` module to create abstract classes
- Inherit from `ABC` to define an abstract class

**Abstract Methods**
- Marked with `@abstractmethod` decorator
- Must be implemented by subclasses
- Cannot be called on the abstract class itself

## Basic Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# dog = Animal()  # TypeError: Can't instantiate abstract class
dog = Dog()
print(dog.make_sound())  # Output: Woof!
```

## Benefits
- Enforces implementation of required methods
- Promotes code consistency and structure
- Enables polymorphism
- Makes code more maintainable
