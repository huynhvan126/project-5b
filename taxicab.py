# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 05/01/2024
# Description: Defined a class that has three private data members x, y, and odometer.
class Taxicab:
    """Represent a Taxicab with x and y coordinates and an odometer reading."""
    def __init__(self, x, y):
        """Initialize the Taxicab with x and y coordinates and sets the odometer to zero."""
        self._x_coord = x
        self._y_coord = y
        self._odometer = 0
    def get_x_coord(self):
        """Return the x coordinate of the taxicab."""
        return self._x_coord
    def get_y_coord(self):
        """Return the y coordinate of the taxicab."""
        return self._y_coord
    def get_odormeter(self):
        """Return the odometer of the taxicab."""
        return self._odometer
    def move_x(self, distance):
        """Move the taxicab horizontally by the given distance."""
        self._x_coord += distance
        self._odometer += abs(distance)
    def move_y(self, distance):
        """Move the taxicab vertically by the given distance."""
        self._y_coord += distance
        self._odometer += abs(distance)
