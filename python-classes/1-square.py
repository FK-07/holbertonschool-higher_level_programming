#!/usr/bin/python3
"""Square modulunu təyin edən sənəd."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size):
        """Kvadratı həcm (size) ilə başlatmaq üçün konstruktor.

        Args:
            size: Kvadratın tərəf ölçüsü.
        """
        self.__size = size
