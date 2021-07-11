"""
Calculate area of given triangle.
Create a function t_area that will take a string which will represent triangle,
find area of the triangle, one space will be equal to one length unit.
The smallest triangle will have one length unit.
"""


def t_area(t_str: str) -> float:
    """Calculate area of a triangle (basic).

    Args:
        t_str: <str> triangle shape as a string.

    Returns: <float> triangle area.
    """
    rows = t_str.split('\n')[2:-1]
    base = rows[-1].count(' ')
    height = sum(map(lambda string: ' ' in string, rows))
    return (base * height) / 2


def t_area_eff(t_str: str) -> float:
    """Calculate area of a triangle (efficient).

    Args:
        t_str: <str> triangle shape as a string.

    Returns: <float> triangle area.
    """
    return (t_str.count('\n') - 2) ** 2 / 2


if __name__ == '__main__':
    string = '\n.\n. .\n. . .\n. . . .\n. . . . .\n'
    print(t_area(string))
    print(t_area_eff(string))
