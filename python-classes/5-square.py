#!/usr/bin/python3
"""Module that defines a Square class with my_print method."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of a side of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculate and return the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters to stdout."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
