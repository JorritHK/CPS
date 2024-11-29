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

    # == Debug Logging ==#

    def debug(self, text: str):
        self.logger.info(text)

    def debug_real(self, name: str, value):
        self.debug(f"DEBUG: Var {name} currently has value: {value}")

    def debug_bool(self, name: str, value):
        self.debug_real(name, value)

    def debug_coord(self, name: str, x: float, y: float):
        self.debug(f"DEBUG Coord {name}: ({x}, {y})")

    # == Simple util functions ==#
    def abs_real(self, x: float):
        return abs(x)

    def ease_out_exp(
        self, distance: float, total_distance: float, exponent: int = 2
    ) -> float:
        if total_distance == 0:
            return 0

        diff_factor = (total_distance - distance) / total_distance

        return 1 - diff_factor**exponent

    # == Initial calibration frame of reference ==#

    def set_calibration(
        self, start_x, start_y, zero_south_degree, laser_deg_offset
    ):
        if self.calibration:
            self.logger.warning(
                "Calibrating again even though this has already been done. "
                "Previous values will be overwritten"
            )

        if zero_south_degree > 180 or zero_south_degree < -180:
            raise Exception(
                f"Incorrect value for Zero South calibration: {zero_south_degree}"
            )

        self.calibration = Calibration(
            coord=Coord(start_x, start_y),
            zero_south_degree=zero_south_degree,
            laser_deg_offset=laser_deg_offset,
        )

    def relative_yaw(self, yaw: float, zero_south_degree: float = None):
        """Translates the 'objective' imu yaw to the yaw relative to the south
        degree we calibrated on"""

        if not zero_south_degree:
            zero_south_degree = self.calibration.zero_south_degree

        yaw_from_south = yaw - zero_south_degree
        if yaw_from_south > 180:
            return -180 + (yaw_from_south - 180)
        if yaw_from_south < -180:
            return 180 + (yaw_from_south + 180)
        return yaw_from_south

    def calc_yaw_rotation(self, yawA: float, yawB: float):
        a = yawA - yawB
        return (a + 180) % 360 - 180

    # == Grid positioning ==#
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

        current = Coord(current_x, current_y)
        grid_x, grid_y = self.grid_position(current, debug=False)
        distance: Coord = current - Coord(
            grid_x * self.grid_size, grid_y * self.grid_size * -1
        )

        return math.sqrt(distance.x**2 + distance.y**2)

    # == Orientation ==#
    def calc_orientation(self, yaw: float, south_degree: float = None) -> int:
        """Finds the current orientation of the robot, with the meaning:
        - north = 0, east = 1, south = 2, west = 3
        - normalized_yaw: north=180, east=90, west=-90, south=0
        (counter clockwise)
        - We use south_degree to calibrate the robot
        """

        if not south_degree:
            south_degree = self.calibration.zero_south_degree

        yaw_from_south = yaw - south_degree

        # Convert
        orientation: int = int(round((-yaw_from_south + 180) / 90) % 4)

        self.debug(
            f"GRID: Robot facing {Orientation(orientation).name} "
            f"({orientation}) for yaw = {yaw}"
        )
        self.debug(f"GRID: Off orientation by: {yaw_from_south % 90}")

        return int(orientation)

    def orientation_to_yaw(self, orientation: int):
        if orientation < 0 or orientation > 4:
            raise Exception(f"Orientation of {orientation} is not valid")
        direction = Orientation(orientation)

        if direction == Orientation.NORTH:
            return 180
        if direction == Orientation.EAST:
            return 90
        if direction == Orientation.SOUTH:
            return 0
        if direction == Orientation.WEST:
            return -90
        raise Exception("Invalid orientation")

    def direction_has_wall(
        self, distance: float, grid_size: float = None, margin: float = 0.20
    ):
        """Reusable function, which specifies our way to get whether a wall
        exists in a certain direction based on lidar data"""

        if not grid_size:
            grid_size = self.grid_size

        # Distance of 4m encodes that there is no valid info,
        # so we return -1 (meaning no information)
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
