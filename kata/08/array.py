"""
Your task is to sum odd values form an array and multiply even values.

# odd of [1, 2, 3, 4] -> 4
# even of [1, 2, 3, 4] -> 8

-----------------------------------
For doctests run following command:
python -m xdoctest -v array.py
or
python3 -m xdoctest -v array.py

For manual testing run:
python array.py
"""
from abc import ABC, abstractmethod
from typing import List
from functools import reduce


class Array(ABC):
    """Represent abstraction of an array."""

    @abstractmethod
    def sum_odd(self) -> int:
        """Sums only odd values in array."""
        pass

    @abstractmethod
    def multiply_even(self) -> int:
        """Multiplies only even numbers."""
        pass


class ArrayCommon(Array):
    def __init__(self, array: List[int]) -> None:
        self._array = array

    def sum_odd(self) -> int:
        """
        Examples:
             >>> assert ArrayCommon([1, 2, 3, 4]).sum_odd() == 4
             >>> assert ArrayCommon([5, 6, 7, 8]).sum_odd() == 12
        """
        odd: int = 0
        for number in self._array:  # type: int
            if number % 2:
                odd += number
        return odd

    def multiply_even(self) -> int:
        """
        Examples:
             >>> assert ArrayCommon([1, 2, 3, 4]).multiply_even() == 8
             >>> assert ArrayCommon([5, 6, 7, 8]).multiply_even() == 48
        """
        even: int = 1
        for number in self._array:  # type: int
            if not number % 2:
                even *= number
        return even


class ArrayPythonic(Array):
    def __init__(self, array: List[int]) -> None:
        self._array = array

    def sum_odd(self) -> int:
        """
        Examples:
             >>> assert ArrayCommon([1, 2, 3, 4]).sum_odd() == 4
             >>> assert ArrayCommon([5, 6, 7, 8]).sum_odd() == 12
        """
        return sum(number for number in self._array if number % 2)

    def multiply_even(self) -> int:
        """
        Examples:
             >>> assert ArrayCommon([1, 2, 3, 4]).multiply_even() == 8
             >>> assert ArrayCommon([5, 6, 7, 8]).multiply_even() == 48
        """
        return reduce(lambda first, second: first * second, (number for number in self._array if not number % 2))


if __name__ == "__main__":
    input_: List[int] = [1, 2, 3, 4]
    array_common: Array = ArrayCommon(input_)
    array_pythonic: Array = ArrayPythonic(input_)
    print(array_common.sum_odd())
    print(array_common.multiply_even())
    print(array_pythonic.sum_odd())
    print(array_pythonic.multiply_even())
