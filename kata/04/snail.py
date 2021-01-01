"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element,
traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
"""
from typing import List, Sequence


def snail(arrays: List[List[int]]) -> List[int]:
    """Sort array in snail approach.

    Examples:
        >>>
        >>> assert snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    """
    result: List[int] = list()
    while len(arrays):
        result.extend(arrays[0])  # move right
        del arrays[0]

        if len(arrays):  # move down
            for array in arrays:
                result.append(array[-1])
                del array[-1]

            if arrays[-1]:  # move left
                result.extend(arrays[-1][::-1])
                del arrays[-1]

            for array in arrays[::-1]:  # move up
                result.append(array[0])
                del array[0]
    return result


def snail_pythonic(arrays: List[List[int]]) -> List[int]:
    """Sort array in snail approach (pythonic).

    Examples:
        >>>
        >>> assert snail_pythonic([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    """
    return (
        arrays[0] + snail_pythonic(list(map(list, zip(*arrays[1:])))[::-1])
        if arrays
        else []
    )


def snail_pythonic_v2(arrays: List[List[int]]) -> List[int]:
    """Sort array in snail approach (pythonic v2).

    Examples:
        >>>
        >>> assert snail_pythonic_v2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    """
    result: List[int] = list()
    while arrays:
        result.extend(arrays.pop(0))
        arrays: List[Sequence[int]] = list(zip(*arrays))
        arrays.reverse()
    return result


if __name__ == "__main__":
    print(snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(snail_pythonic([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(snail_pythonic_v2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
