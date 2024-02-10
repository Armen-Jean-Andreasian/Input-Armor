from typing import Iterable, LiteralString
from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from .detection_data import SqlList, JavaScriptHtmlList


def anti_injection_check(rabbit: LiteralString,
                         language_data: Type[SqlList | JavaScriptHtmlList],
                         check_level: int,
                         white_list: Iterable = None,
                         black_list: Iterable = None):
    """
    Checks for SQL-injection-specific keywords and expressions.
    Recommended to run after `advanced_check`.

    :param language_data: The injection-type specific class containing soft_list and full_list attributes
    :param rabbit: The string that needs to be checked.
    :param check_level: Identifies the level of check.
        Possible values: 1 and 2. Where:
        1: soft check: Checks against a basic small list of 13 items.
        2: hard check: Checks against a large list of 159 items.
    :param white_list: An iterable with values that are allowed to have.
    :param black_list: An iterable with custom values that are not allowed to have.

    """
    # initializing the list_of_forbidden_items
    if check_level == 1:
        list_of_forbidden_items = language_data.soft_list
    elif check_level == 2:
        list_of_forbidden_items = language_data.full_list
    else:
        raise ValueError("The argument of check_level should be 0 or 1")

    # checking if both black_list and white_list exist so do not have matching items
    if white_list and black_list:
        for black_listed_item in black_list:
            if black_listed_item in white_list:
                raise ValueError("Matching values in white_list and black_list")

    # if any of black_list or white_list does not exist, assigning dummy tuples to it.
    # This allows to use 'in' keyword.
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
    return None
