def length_check(rabbit: str, fixed_length: int) -> None:
    """
    Raises an AssertionError if the length of the string exceeds the fixed length.
    Also raises an AssertionError if the string consist of whitespace(s) only.
    """
    assert 0 < len(rabbit.strip()) < fixed_length, f"The string {rabbit} failed the {length_check.__name__}"
    return None
