from typing import Iterable, LiteralString
from checks import encoding_check
from checks import length_check
from checks import logical_expression_check
from checks import punctuation_symbols_check
from checks import presence_check
from ban_list import SqlList


class InputArmor:
    @staticmethod
    def advanced_check(
            rabbit: LiteralString,
            check_encoding: bool = False,
            check_length: bool = False, fixed_length: int = 10,
            check_for_logical_expressions: bool = False,
            check_for_punctuation_symbols: bool = False,
            check_for_undefined_value: bool = False, possible_values: Iterable = None) -> None:
        """
        Provides advanced string check-ups.
        Raises AssertionError if any of checks fail. Returns None if all checks pass.

        :param rabbit: The string that needs to be checked.
        :param check_encoding: If the encoding of `rabbit` is utf-8.
        :param check_length: If the length of `rabbit` (stripped) is less than `fixed_length` param, and more than zero.
        :param fixed_length: By default, it's 10 (Chars. Spaces excluded).
        :param check_for_logical_expressions:
        :param check_for_punctuation_symbols:
        :param check_for_undefined_value: Checks if `rabbit` is present in `possible_values` param.
        :param possible_values: The iterable object to look for `rabbit`'s presence.
        """

        if type(rabbit) is not str:
            raise TypeError(f"Non-string value was found in {rabbit}")
        else:
            if check_encoding:
                assert encoding_check(rabbit) is None

            if check_length:
                assert length_check(rabbit, fixed_length) is None

            if check_for_logical_expressions:
                assert logical_expression_check(rabbit) is None

            if check_for_punctuation_symbols:
                assert punctuation_symbols_check(rabbit)

            if check_for_undefined_value:
                if possible_values is None:
                    raise TypeError(f"Iterable expected for possible_values. Found None.")
                else:
                    assert presence_check(rabbit, possible_values) is None

        return None

    @staticmethod
    def sql_injection_check(rabbit: LiteralString,
                            check_level: int = 0,
                            white_list: Iterable = None,
                            black_list: Iterable = None):
        """
        Checks for SQL-injection-specific keywords and expressions.
        Recommended to run after `advanced_check`.

        :param rabbit: The string that needs to be checked.
        :param check_level: Identifies the level of check.
            Possible values: 1 and 2. Where:
            1: soft check: Checks against a basic small list of 13 items.
            2: hard check: Checks against a large list of 159 items.
        :param white_list: An iterable with values that are allowed to have.
        :param black_list: An iterable with custom values that are not allowed to have.

        """
        # identifying the list_of_forbidden_items
        if check_level == 1:
            list_of_forbidden_items = SqlList.soft_list
        elif check_level == 2:
            list_of_forbidden_items = SqlList.full_list
        else:
            raise ValueError("The argument of check_level should be 0 or 1")

        # checking if both black_list and white_list exist and do not have matching items
        if white_list and black_list:
            for black_listed_item in black_list:
                if black_listed_item in white_list:
                    raise ValueError("Matching values in white_list and black_list")

        # if any of black_list or white_list does not exist, assigning dummy tuples to it.
        # This allows to use 'in' keyword further.
        else:
            if white_list is None:
                white_list = tuple()
            if black_list is None:
                black_list = tuple()

        # first check. Looking for forbidden characters against the SqlList
        for forbidden_item in list_of_forbidden_items:
            if forbidden_item in rabbit and forbidden_item not in white_list:
                raise AssertionError(f"{forbidden_item} found in {rabbit}")

        # second check. Looking for forbidden characters against the black_list
        for forbidden_item in black_list:
            if forbidden_item in rabbit:
                raise AssertionError(f"{forbidden_item} found in {rabbit}")
