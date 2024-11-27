from enum import Enum
import math
import logging

from typing import Literal, Tuple

Direction = Literal["north", "west", "south", "east"]


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


class Calibration:
    coord: Coord
    zero_south_degree: float
    laser_deg_offset: float

    def __init__(self, coord, zero_south_degree, laser_deg_offset) -> None:
        self.coord = coord
        self.zero_south_degree = zero_south_degree
        self.laser_deg_offset = laser_deg_offset


class Orientation(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Callback:
    def __init__(self):
        logging.basicConfig(filename="debug_robot.log", level=logging.DEBUG)
        self.logger = logging.getLogger("debug")
        self.calibration: Calibration = None
        self.grid_size = 0.48

    def debug(self, text: str):
        self.logger.info(text)

    def debug_real(self, name: str, value):
        self.debug(f"DEBUG: Var {name} currently has value: {value}")

    def debug_bool(self, name: str, value):
        self.debug_real(name, value)

    def debug_coord(self, name: str, x: float, y: float):
        self.debug(f"DEBUG Coord {name}: ({x}, {y})")

    def set_calibration(
        self, start_x, start_y, zero_south_degree, laser_deg_offset
    ):
        self.calibration = Calibration(
            coord=Coord(start_x, start_y),
            zero_south_degree=zero_south_degree,
            laser_deg_offset=laser_deg_offset,
        )

    def grid_position(
        self,
        current: Coord,
        y_direction: Direction = "south",
        x_direction: Direction = "east",
        start: Coord = None,
        debug=True,
    ) -> Tuple[int, int]:
        if not start:
            start = self.calibration.coord

        print(start)
        print(current)

        diff: Coord = start - current
        grid_x: int = round(diff.x / self.grid_size)
        grid_y: int = round(diff.y / self.grid_size)

        if y_direction == "south":
            grid_x *= -1
        if x_direction == "west":
            grid_y *= -1

        distance: Coord = diff - Coord(
            grid_x * self.grid_size, grid_y * self.grid_size
        )

        if debug:
            self.debug(f"GRID: In ({grid_x}, {grid_y}). Distance: {distance}")

        return grid_x, grid_y

    def grid_position_column(self, current_x: float, start_x: float = None):
        if not start_x:
            start_x = self.calibration.coord.x

        x, _ = self.grid_position(
            Coord(current_x, 0), start=Coord(start_x, 0), debug=False
        )
        return x

    def grid_position_row(self, current_y, start_y: float = None):
        if not start_y:
            start_y = self.calibration.coord.y
        _, y = self.grid_position(
            Coord(0, current_y), start=Coord(0, start_y), debug=False
        )
        return y

    def distance_to_grid_center(self, current_x: float, current_y: float):

        diff: Coord = self.calibration.coord - Coord(current_x, current_y)
        grid_x, grid_y = self.grid_position(
            Coord(current_x, current_y), debug=False
        )
        distance: Coord = diff - Coord(
            grid_x * self.grid_size, grid_y * self.grid_size
        )

        return math.sqrt(distance.x**2 + distance.y**2)

    def calc_orientation(self, yaw: float, south_degree: float = None) -> int:
        """Finds the current orientation of the robot, with the meaning:
        - north = 0, east = 1, south = 2, west = 3
        - We use south_degree to calibrate the robot
        """

        if not south_degree:
            south_degree = self.calibration.zero_south_degree

        yaw_south_calibrated = yaw - south_degree
        orientation: int = round((yaw_south_calibrated + 180) / 90 % 4)

        self.debug(
            f"GRID: Robot facing {Orientation(orientation).name} "
            f"({orientation}) for yaw = {yaw}"
        )
        self.debug(f"GRID: Off orientation by: {yaw_south_calibrated % 90}")

        return int(orientation)

    def direction_has_wall(
        self, distance: float, grid_size: float = None, margin: float = 0.20
    ):

        if not grid_size:
            grid_size = self.grid_size

        # Distance of 4m encodes that there is no valid info, so we return -1 (meaning no information)
        if distance == 4:
            return -1

        expected_distance = grid_size / 2

        self.debug(
            "GRID: Assessing if there is a wall with distance: "
            f"{distance}, margin: {margin}, expected: {expected_distance}"
        )

        if distance < (expected_distance + margin):
            return 1
        return 0
