"""
Program allows to find first duplicate in an array
"""
from typing import Sequence, Any


def find_first_duplicate(sequence: Sequence[Any]) -> Any:
    """Finds first duplicate in an array (high complexity).

    Args:
        sequence: an array

    Returns:
        first duplicate item

    Examples:
        >>> assert find_first_duplicate("abccd") == "c"
        >>> assert find_first_duplicate([1, 2, 3, 4, 4, 5]) == 4
    """
    for top in range(len(sequence) - 1):  # type: int
        for inner in range(len(sequence) - 1):  # type: int
            if top != inner and sequence[top] == sequence[inner]:
                return sequence[inner]
    return -1


def find_first_duplicate_v2(sequence: Sequence[Any]) -> Any:
    """Finds first duplicate in an array (high complexity).

    Args:
        sequence: an array

    Returns:
        first duplicate item

    Examples:
        >>> assert find_first_duplicate_v2("abccd") == "c"
        >>> assert find_first_duplicate_v2([1, 2, 3, 4, 4, 5]) == 4
    """
    for top_index, top in enumerate(sequence):  # type: int, Any
        for inner_index, inner in enumerate(sequence):  # type: int, Any
            if top_index != inner_index and top == inner:
                return top
    return -1


if __name__ == "__main__":
    print(find_first_duplicate("abccd"))
    print(find_first_duplicate_v2("abccd"))
