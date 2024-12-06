from enum import Enum
from typing import Literal


class Coord:
    x: float
    y: float

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Coord({self.x}, {self.y})"


class Calibration:
    coord: Coord
    zero_south_degree: float
    laser_deg_offset: float

    def __init__(self, coord, zero_south_degree, laser_deg_offset) -> None:
        self.coord = coord
        self.zero_south_degree = zero_south_degree
        self.laser_deg_offset = laser_deg_offset


Direction = Literal["north", "west", "south", "east"]


class Orientation(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
