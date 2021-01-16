"""
Based on those 3 values you have to return a string, that describes which operation was used to get the given result.

The possible return strings are: "addition", "subtraction", "multiplication", "division".

Notes
In case of division you should expect that the result of the operation is obtained by using / operator on the input values - no manual data type conversion or rounding should be performed.
Cases with just one possible answers are generated.
Only valid arguments will be passed to the function.
Only valid arguments will be passed to the function!
"""


def calc_type(a: int, b: int, res: int) -> str:
    """Find the calculation type by the result.

    Examples:
        >>> assert calc_type(10, 2, 5) == 'division'
    """
    return {
        a - b: 'subtraction',
        a + b: 'addition',
        a / b: 'division',
        a * b: 'multiplication',
    }[res]


if __name__ == '__main__':
    print(calc_type(10, 2, 5))
