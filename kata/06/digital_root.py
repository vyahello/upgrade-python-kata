"""
In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. 
Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
"""


def digital_root(number: int) -> int:
    """Sums all numbers in given number.

    Args:
        number (int): given number

    Examples:
        >>> assert digital_root(166) == 4
    """
    if len(str(number)) > 1:
        return digital_root(sum(map(int, str(number))))
    return number


if __name__ == "__main__":
    print(digital_root(16))
