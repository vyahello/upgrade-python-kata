"""
Calculates distance between two points.

y
|  . (x1, y1)
|
|           . (x2, y2)
|______________ x

"""
from typing import NamedTuple
import math


class Coordinate(NamedTuple):
    """Represents coordinate element."""

    x_axi: int
    y_axi: int


def calculate_distance(point_one: Coordinate, point_two: Coordinate) -> float:
    """Returns distance between two points

    Args:
        point_one: coordinate of first point
        point_two: coordinate of second point

    Examples:
        >>> assert calculate_distance(Coordinate(x_axi=1, y_axi=5), Coordinate(x_axi=5, y_axi=1)) == 5.66
    """
    return round(
        math.sqrt(
            (point_two.x_axi - point_one.x_axi) ** 2
            + (point_two.y_axi - point_one.y_axi) ** 2
        ),
        2,
    )


if __name__ == "__main__":
    print(
        calculate_distance(
            Coordinate(x_axi=1, y_axi=5), Coordinate(x_axi=5, y_axi=1)
        )
    )  # 5.66
