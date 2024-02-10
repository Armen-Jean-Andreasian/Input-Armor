import string


def punctuation_symbols_check(rabbit: str) -> None:
    """Raises an AssertionError if the string contains a punctuation symbol"""
    assert rabbit.isalnum() and (x not in string.punctuation for x in rabbit), \
        f"The string {rabbit} failed the {punctuation_symbols_check.__name__}"
    return None
