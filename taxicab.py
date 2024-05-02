# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 05/01/2024
# Description: Defined a class that has three private data members x, y, and odometer.
class Taxicab:
    """Represent a Taxicab with x and y coordinates and an odometer reading."""
    def __init__(self, x, y):
        """Initialize the Taxicab with x and y coordinates and sets the odometer to zero."""
        self._x_coordinate = x
        self._y_coordinate = y
        self._odormeter = 0
    def get_x_coord(self):
        """Return the x coordinate of the taxicab."""
        return self._x_coordinate
    def get_y_coord(self):
        """Return the y coordinate of the taxicab."""
        return self._y_coordinate
    def get_odormeter(self):
        """Return the odometer of the taxicab."""
        return self._odormeter
    def move_x(self, distance):
        """Move the taxicab horizontally by the given distance."""
        self._x_coordinate += distance
        self._odormeter += abs(distance)
    def move_y(self, distance):
        """Move the taxicab vertically by the given distance."""
        self._y_coordinate += distance
        self._odormeter += abs(distance)