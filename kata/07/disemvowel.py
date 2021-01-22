"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, 
neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""
_VOWELS: str = 'aAiIeEoOuU'


def disemvowel(string: str) -> str:
    """Removes vowels from the string.

    Example:
        >>> assert disemvowel('LOL LOL') == 'LL LL'
    """

    return ''.join(
        consonant for consonant in string if consonant not in _VOWELS
    )


def disemvowel_classic(string: str) -> str:
    """Removes vowels from the string (classic approach).

    Example:
        >>> assert disemvowel('LOL LOL') == 'LL LL'
    """
    for next_vowel in _VOWELS:  # type: str
        string = string.replace(next_vowel, '')
    return string


if __name__ == '__main__':
    print(disemvowel('LOL LOL'))
