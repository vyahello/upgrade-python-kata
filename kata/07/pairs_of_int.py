"""
Write a function generatePairs (Javascript) / generate_pairs (Python / Ruby)
that accepts an integer argument n and generates an array containing the pairs
of integers [a, b] that satisfy the following conditions:

0 <= a <= b <= n
The pairs should be sorted by increasing values
of a then increasing values of b.

For example,

generate_pairs(2) should return
[ [0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2] ]
"""
from typing import List


def generate_pairs(number: int) -> List[List[int]]:
    """Generate all pairs of number sequence.

    Args:
        number: <int> the number

    Returns: <list> a sequence

    Examples:
        >>> assert generate_pairs(1) == [[0, 0], [0, 1], [1, 1]]
    """
    return [
        [top, inner]
        for top in range(number + 1)
        for inner in range(top, number + 1)
    ]


if __name__ == '__main__':
    print(generate_pairs(1))
