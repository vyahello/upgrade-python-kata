"""
Your task to write a function that takes one argument (an array of integers)

It should behave like next one sample:
[1, 1, 2, 2, 2, 10] -> 2

"""
from typing import Sequence, Dict, List


def most_popular_number_common(array: Sequence[int]) -> int:
    """Returns most frequent number from an array.

    Probably worst scenario but works as expected.
    """
    storage: Dict[int, int] = {}
    for number in array:  # type: int
        if number not in storage:
            storage[number] = 0
        storage[number] += 1
    for key, value in storage.items():  # type: int, int
        if value == max(tuple(storage.values())):
            return key


def most_popular_number_naive(array: Sequence[int]) -> int:
    """Returns most frequent number from an array.

    Naive approach.
    """
    counter: int = 0
    first: int = array[0]
    for number in array:  # type: int
        amount: int = array.count(number)
        if amount > counter:
            counter = amount
            first = number
    return first


def most_popular_number_pythonic(array: Sequence[int]) -> int:
    """Returns most frequent number from an array.

    It is the most pythonic way.
    """
    return max(set(array), key=array.count)


if __name__ == "__main__":
    numbers: List[int] = [10, 10, 100, 10, 2, 2, 1]
    print(most_popular_number_common(array=numbers))  # returns 10
    print(most_popular_number_naive(array=numbers))  # returns 10
    print(most_popular_number_pythonic(array=numbers))  # returns 10
