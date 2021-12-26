"""
Implement a function that accepts 3 integer values a, b, c.
The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
"""


def is_triangle(side_one: int, side_two: int, base: int) -> bool:
    """Check if triangle can be built with given sides length.

    Args:
        side_one: <int> first side of triangle.
        side_two: <int> second side of triangle.
        base: <int> base side of triangle.

    Returns: True if triangle can be built with the sides of given length.

    Examples:
        >>> assert is_triangle(1, 2, 2)
        >>> assert is_triangle(3, 2, 2)
    """
    return side_one + side_two > base and side_two + base > side_one and side_one + base > side_two


if __name__ == '__main__':
    is_triangle(1, 2, 2)
    is_triangle(3, 2, 2)
