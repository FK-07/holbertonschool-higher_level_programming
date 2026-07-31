#!/usr/bin/python3
"""Module that defines a Square class with size and position validation."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int): The size of a side of the square. Defaults to 0.
            position (tuple): The (x, y) coordinates. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the current position of the square.

        Returns:
            tuple: The (x, y) coordinates of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with type and value validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculate and return the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters and position coordinates."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
