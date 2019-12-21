"""
You have to write a bunch of decorators to trace execution.

-----------------------------------
For doctests run following command:
python -m xdoctest -v decorators.py
or
python3 -m xdoctest -v decorators.py

For manual testing run:
python decorators.py
"""
from typing import Callable, Generator, Any
from functools import wraps

_Generator = Generator[str, None, None]
_CallableGenerator = Callable[[], _Generator]


def trace(func: Callable[[Any], Any]) -> _CallableGenerator:
    """Traces function execution."""

    @wraps(func)
    def wrapper(*args, **kwargs) -> _Generator:
        name: str = func.__name__
        yield f"Entering {name} function with [{args} {kwargs}] arguments"
        yield f"Result is '{func(*args, **kwargs)}'"
        yield f"Exiting {name} function"

    return wrapper


def multiply_by(multiplier: int) -> Callable[[Any], Any]:
    """Multiplies a number."""

    def decorator(func: Callable[[Any], Any]) -> _CallableGenerator:
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name: str = func.__name__
            yield f'Calling "{func_name}({args[0]}, {args[1]})" function'
            yield f'"{func_name}" function is multiplied by {multiplier}'
            yield f"Result is {func(*args, **kwargs) * multiplier}"

        return wrapper

    return decorator


@trace
def say_hello(word: str) -> str:
    """Says hello.

    Examples:
        >>> tuple(say_hello("Python"))
        >>> ("Entering say_hello function with [('Python',) {}] arguments", "Result is 'Hello Python'", 'Exiting say_hello function')
    """
    return f"Hello {word}"


@multiply_by(multiplier=3)
def add(a: int, b: int) -> int:
    """Adds two items.

    Examples:
        >>> tuple(add(2, 3))
        >>> ('Calling "add(2, 3)" function', '"add" function is multiplied by 3', 'Result is 15')
    """
    return a + b


if __name__ == "__main__":
    print(tuple(say_hello("Python")))
    print(tuple(add(2, 3)))
