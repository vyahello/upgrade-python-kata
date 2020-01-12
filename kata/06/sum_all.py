"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Finish the solution so th
"""


def sum_multiples_of_3_and_5(number: int) -> int:
    """
    Examples:
         >>> assert sum_multiples_of_3_and_5(10) == 23
    """
    return sum(next_number for next_number in range(number) if next_number % 3 == 0 or next_number % 5 == 0)


if __name__ == "__main__":
    print(sum_multiples_of_3_and_5(10))
