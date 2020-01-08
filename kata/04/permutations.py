"""
In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
"""
from typing import List
from itertools import permutations as options


def permutations(string: str) -> List[str]:
    """
    Examples:
        >>> assert permutations('aabb') == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    """
    return sorted(set("".join(option) for option in options(string)))


if __name__ == "__main__":
    print(permutations("aabb"))
