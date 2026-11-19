
"""
Program: Identify Object's Class Using type()
Description: Identify the class of different objects
using Python's built-in type() function.
"""


class Dog:
    """Represent a Dog object."""
    pass


class Cat:
    """Represent a Cat object."""
    pass


class Vehicle:
    """Represent a Vehicle object."""
    pass


def main():
    """Create objects and display their class names."""

    # Create objects
    d = Dog()
    c = Cat()
    v = Vehicle()

    # Identify object types
    print(f"d is of type: {type(d).__name__}")
    print(f"c is of type: {type(c).__name__}")
    print(f"v is of type: {type(v).__name__}")


if __name__ == "__main__":
    main()