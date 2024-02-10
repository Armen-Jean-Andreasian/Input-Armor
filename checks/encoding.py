def encoding_check(rabbit: str) -> None:
    """Raises an AssertionError if the encoding is not utf-8"""
    assert type(rabbit.encode(encoding='utf-8')) is bytes, f"The string {rabbit} failed the {encoding_check.__name__}"
    return None
