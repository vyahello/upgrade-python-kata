"""
You are given a dictionary/hash/object containing some languages and your test results in the given languages.
Return the list of languages where your test score is at least 60, in descending order of the results.

Note: the scores will always be unique (so no duplicate values)
"""


def my_languages(results: dict) -> list:
    """Returns all languages with score at least 60

    Args:
        results (dict): mapped languages with scores

    Examples:
        >>> assert my_languages({"Java": 10, "Ruby": 80, "Python": 65}) == ["Ruby", "Python"]
    """
    return [
        language
        for language, score in sorted(
            results.items(), key=lambda pair: pair[1], reverse=True
        )
        if score > 59
    ]


if __name__ == "__main__":
    print(my_languages({"Java": 10, "Ruby": 80, "Python": 65}))
