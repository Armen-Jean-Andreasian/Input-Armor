def keyword_check(rabbit: str) -> None:
    """Raises an AssertionError if a keyword found.
    Attention: this method doesn't cover all keywords, but the most used ones."""
    rabbit = rabbit.lower()

    keywords_list = (
        'while',
        'as',
        'if',
        'else',
        'import',
        'select',
        'do',
    )
    rabbit = rabbit.lower().strip().split()

    for item in rabbit:
        if item in keywords_list:
            raise AssertionError(f"The string {rabbit} failed the {keyword_check.__name__}"
                                 f"Keyword {item} found in {rabbit}." )

    return None
