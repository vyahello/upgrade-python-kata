"""
Write a function, which takes a non-negative integer (seconds) as
input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""


def make_readable(value: int) -> str:
    """Make readable time.

    Examples:
        >>> assert make_readable(359999) == "99:59:59"
    """
    minutes, seconds = divmod(value, 60)  # type: int, int
    hours, minutes = divmod(minutes, 60)  # type: int, int
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def make_readable_pythonic(value: int) -> str:
    """Make readable time (pythonic).

    Examples:
        >>> assert make_readable(359999) == "99:59:59"
    """
    return f"{value / 3600:02d}:{value / 60 % 60:02d}:{value % 60:02d}"


if __name__ == "__main__":
    print(make_readable(359999))
    print(make_readable_pythonic(359999))
