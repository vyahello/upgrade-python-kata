"""
productFib(714) # should return (21, 34, True),
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, False),
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
"""
from typing import List, Any


def fibonacci(number: int) -> int:
    """Returns fibonacci number.

    Args:
        number: number to count fibonacci sequence
    """
    counter, handler = 1, 1
    for next_number in range(number - 1):  # type: int
        counter, handler = handler, counter + handler
    return counter


def product_fibonacci(product: int) -> List[Any]:
    """Produce fibonacci sequence mapper

    Returns: a list of fibonacci mapping

    Examples:
        >>> assert product_fibonacci(800) == [34, 55, False]
    """
    if not product:
        return [0, 1, True]
    current_value: int = 0
    counter: int = 0
    fibonacci_one = fibonacci_two = 0  # type: int
    while current_value < product:
        counter += 1
        fibonacci_one: int = fibonacci(counter)
        fibonacci_two: int = fibonacci(counter + 1)
        current_value: int = fibonacci_one * fibonacci_two
    if current_value == product:
        return [fibonacci_one, fibonacci_two, True]
    return [fibonacci_one, fibonacci_two, False]


if __name__ == "__main__":
    print(product_fibonacci(800) == [34, 55, False])
