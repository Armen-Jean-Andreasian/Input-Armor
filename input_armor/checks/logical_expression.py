import re


def logical_expression_check(rabbit: str) -> None:
    """Raises an AssertionError if a logical expression found in a single word."""
    rabbit = rabbit.lower()
    pattern = r'(\b\w+[><!=]=?[><!=]?\w+\b)|(\b\w+(?:is|==|===)\w+\b)'
    if re.search(pattern, rabbit):
        raise AssertionError(f"Logical expression found in a {rabbit} word")
    return None
