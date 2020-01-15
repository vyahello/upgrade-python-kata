"""
The Padovan sequence is the sequence of integers P(n) defined by the initial values

P(0)=P(1)=P(2)=1

and the recurrence relation

P(n)=P(n-2)+P(n-3)

The first few values of P(n) are

1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114, 151, 200, 265, ...
"""


def padovan(number: int) -> int:
    """
    Examples:
        >>> assert padovan(2) == 1
        >>> assert padovan(5) == 3
    """
    result = [0, 1, 1]
    for c in range(2, number):
        result.append(result[0] + result[1])
        del result[0]
    return result[0] + result[1]


def padovan_pythonic(number: int) -> int:
    """
    Examples:
        >>> assert padovan_pythonic(2) == 1
        >>> assert padovan_pythonic(5) == 3
    """
    p0 = p1 = p2 = 1
    for _ in range(number):
        p0, p1, p2 = p1, p2, p0 + p1
    return p0


if __name__ == "__main__":
    print(padovan(5))
    print(padovan_pythonic(5))
