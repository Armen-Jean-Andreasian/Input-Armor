from typing import Iterable, LiteralString

from lib.checks import encoding_check
from lib.checks import length_check
from lib.checks import logical_expression_check
from lib.checks import punctuation_symbols_check
from lib.checks import presence_check
from lib.checks import keyword_check

from .specific_checks import anti_injection_check
from .specific_checks.detection_data import SqlList
from .specific_checks.detection_data import JavaScriptHtmlList


class InputArmor:
    @staticmethod
    def advanced_check(
            rabbit: LiteralString,
            check_encoding: bool = True,
            check_length: bool = True, max_length: int = 10,
            check_for_logical_expressions: bool = True,
            check_for_keywords: bool = False,
            check_for_punctuation_symbols: bool = True,
            check_for_undefined_value: bool = False, possible_values: Iterable = None) -> None:
        """
        Provides advanced string check-ups.
        Raises AssertionError if any of checks fail. Returns None if all checks pass.

        :param rabbit: The string that needs to be checked.
        :param check_encoding: If the encoding of `rabbit` is utf-8.
        :param check_length: If the length of `rabbit` (stripped) is less than `fixed_length` param, and more than zero.
        :param max_length: By default, it's 10 (Chars. Spaces excluded).
        :param check_for_keywords:
        :param check_for_logical_expressions:
        :param check_for_punctuation_symbols:
        :param check_for_undefined_value: Checks if `rabbit` is present in `possible_values` param.
        :param possible_values: The iterable object to look for `rabbit`'s presence.
        """

        if type(rabbit) is not str:
            raise TypeError(f"Non-string value was found in {rabbit}")

        if check_encoding:
            assert encoding_check(rabbit=rabbit) is None
            print('checked encoding')

        if check_length:
            assert length_check(rabbit, max_length) is None

        if check_for_logical_expressions:
            assert logical_expression_check(rabbit) is None

        if check_for_keywords:
            assert keyword_check(rabbit) is None

        if check_for_punctuation_symbols:
            assert punctuation_symbols_check(rabbit) is None

        if check_for_undefined_value:
            if possible_values is None:
                raise TypeError(f"Iterable expected for possible_values. Found None.")
            else:
                assert presence_check(rabbit, possible_values) is None

        return None

    @staticmethod
    def sql_injection_check(rabbit: LiteralString,
                            check_level: int = 1,
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

        anti_injection_check(rabbit=rabbit, white_list=white_list, black_list=black_list, check_level=check_level,
                             language_data=SqlList)
        return None

    @staticmethod
    def html_injection_check(rabbit: LiteralString,
                             check_level: int = 1,
                             white_list: Iterable = None,
                             black_list: Iterable = None):
        """
        Checks for Dom-Manipulation-specific keywords and expressions.
        Recommended to run after `advanced_check`.

        :param rabbit: The string that needs to be checked.
        :param check_level: Identifies the level of check.
            Possible values: 1 and 2. Where:
            1: soft check: Checks against a basic small list of 44 items.
            2: hard check: Checks against a large list of 127 items.
        :param white_list: An iterable with values that are allowed to have.
        :param black_list: An iterable with custom values that are not allowed to have.
        """
        anti_injection_check(rabbit=rabbit, white_list=white_list, black_list=black_list, check_level=check_level,
                             language_data=JavaScriptHtmlList)
        return None
