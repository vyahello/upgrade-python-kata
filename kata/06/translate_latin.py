"""Translate latin numbers to actual numbers."""


def translate_latin_to_number(number: str) -> int:
    """Translate latin number to basic number.

    Args:
        number: <str> latin number.

    Returns: basic number.

    Examples:
        >>> assert translate_latin_to_number('III') == 3
        >>> assert translate_latin_to_number('IV') == 4
        >>> assert translate_latin_to_number('VI') == 6
        >>> assert translate_latin_to_number('XXX') == 30
    """
    latin_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    counter = latin_to_int[number[-1]]
    for n in range(len(number) - 1):  # type: int
        left, right = latin_to_int[number[n]], latin_to_int[number[n + 1]]
        if left >= right:
            counter += left
        else:
            counter -= left
    return counter
