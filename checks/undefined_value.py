from typing import Iterable
import hashlib


def presence_check(rabbit: str, possible_values: Iterable) -> None:
    """Raises an AssertionError if the given string is not mentioned in possible_values"""

    # safe check through hashing
    hashed_rabbit = hashlib.md5(rabbit.encode()).hexdigest()

    try:
        possible_hashes = [hashlib.md5(val.encode()).hexdigest() for val in possible_values]
    except AttributeError as error:
        if str(error) == "'int' object has no attribute 'encode'":
            raise TypeError(f"Non-integer item found in {possible_values}")
        else:
            raise error
    else:
        assert hashed_rabbit in possible_hashes

    # direct check
    assert rabbit in possible_values
    return None

