"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array
with all of the integer's divisors(except for 1 and the number itself), from smallest to largest.

If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in
Haskell and Result<Vec<u32>, String> in Rust).
"""


def divisors(integer: int) -> list:
    """Returns all divisors

    Args:
        integer (int): a number

    Examples:
        >>> assert divisors(12) == [2, 3, 4, 6]
    """
    result: list = [divisor for divisor in range(2, integer - 1) if not integer % divisor]
    if not result:
        return f"{integer} is prime"
    return result


if __name__ == "__main__":
    print(divisors(12))
