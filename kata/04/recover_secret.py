"""
There is a secret string which is unknown to you.
Given a collection of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before
the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain
sufficient information to deduce the original string.

In particular, this means that the secret string will never contain letters that
do not occur in one of the triplets given to you.
"""
from typing import List

StringList = List[str]
ListStringList = List[StringList]


def pass_bigger(array: StringList, first: str, second: str) -> None:
    """Lets bigger value to pass smaller in an array.

    Args:
        array (List[str]): an array
        first (str): first value
        second (str): second value
    """
    if array.index(first) > array.index(second):
        array.remove(first)
        array.insert(array.index(second), first)


def recover_secret(triplets: ListStringList) -> str:
    """Recovers secret string from given triples.

    Args:
        triplets (List[str]): a list of triples

    Examples:
        >>> triplets = [
        ... ['t','u','p'],
        ... ['w','h','i'],
        ... ['t','s','u'],
        ... ['a','t','s'],
        ... ['h','a','p'],
        ... ['t','i','s'],
        ... ['w','h','s']
        ... ]
        >>> assert recover_secret(triplets) == "whatisup"
    """
    unique: StringList = list(set(char for row in triplets for char in row))
    for row in triplets:  # type: StringList
        pass_bigger(unique, row[1], row[2])
        pass_bigger(unique, row[0], row[1])
    return "".join(unique)


def recover_secret_v2(triplets: ListStringList) -> str:
    """Recovers secret string from given triples.

    Args:
        triplets (List[str]): a list of triples

    Examples:
        >>> triplets = [
        ... ['t','u','p'],
        ... ['w','h','i'],
        ... ['t','s','u'],
        ... ['a','t','s'],
        ... ['h','a','p'],
        ... ['t','i','s'],
        ... ['w','h','s']
        ... ]
        >>> assert recover_secret_v2(triplets) == "whatisup"
    """
    unique: StringList = list(set(char for row in triplets for char in row))
    while True:
        counter: int = 0
        for row in triplets:  # type: StringList
            first: int = unique.index(row[0])
            second: int = unique.index(row[1])
            third: int = unique.index(row[2])
            if first > second or second > third:
                counter += 1
                first, second, third = sorted((first, second, third))
                unique[first], unique[second], unique[third] = (
                    row[0],
                    row[1],
                    row[2],
                )
        if not counter:
            return "".join(unique)


if __name__ == "__main__":
    triplets: ListStringList = [
        ["t", "u", "p"],
        ["w", "h", "i"],
        ["t", "s", "u"],
        ["a", "t", "s"],
        ["h", "a", "p"],
        ["t", "i", "s"],
        ["w", "h", "s"],
    ]
    print(recover_secret(triplets))
    print(recover_secret_v2(triplets))
