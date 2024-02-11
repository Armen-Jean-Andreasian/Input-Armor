import codecs


def encoding_check(rabbit: str) -> None:
    """
    Raises an AssertionError if the encoding is not utf-8
    """

    try:
        # UnicodeDecodeError check basic
        assert type(rabbit.encode(encoding='utf-8')) is bytes

        # UnicodeDecodeError check advanced
        assert codecs.encode(rabbit, 'latin1', errors='strict')

        # Additional concat check to trigger TypeError
        assert type(rabbit + "normal_string") is str

    except UnicodeEncodeError as error:
        print('unicode error')
        raise AssertionError(
            f"The string {rabbit} failed the {encoding_check.__name__}",
            f"\n{error}"
        )
    return None


if __name__ == '__main__':
    try:
        encoding_check(rabbit="й, ў, ї")
    except AssertionError:
        print(1)
