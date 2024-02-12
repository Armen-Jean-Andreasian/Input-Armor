import unittest
from input_armor import InputArmor


class TestInputArmor(unittest.TestCase):
    valid_string = "valid_string"
    possible_values = ("apple", "banana", "user")

    def test_advanced_check_valid(self):
        # valid
        self.assertIsNone(InputArmor.advanced_check(rabbit=self.valid_string))
        self.assertIsNone(InputArmor.advanced_check(rabbit=self.valid_string + "123"))
        self.assertIsNone(InputArmor.advanced_check(rabbit="B" + self.valid_string + "123"))

    def test_advanced_check_non_string(self):
        # non string input
        with self.assertRaises(TypeError):
            InputArmor.advanced_check(set(self.valid_string))
            InputArmor.advanced_check(TypeError)
            InputArmor.advanced_check(set(self.valid_string))

    def test_advanced_check_wrong_encoding(self):
        # non utf-8 input
        with self.assertRaises(AssertionError):
            InputArmor.advanced_check(rabbit="й, ў, ї")
            InputArmor.advanced_check(rabbit="აბგდევ")
            InputArmor.advanced_check(rabbit="صباح الخير")

    def test_advanced_check_wrong_length(self):
        # length test

        self.assertIsNone(InputArmor.advanced_check(rabbit="store", check_length=True, max_length=15))

        with self.assertRaises(AssertionError):
            InputArmor.advanced_check(rabbit="hello", check_length=True, max_length=3)
            InputArmor.advanced_check(rabbit="wdwdcdcsdcsdss", check_length=True)

    def test_advanced_check_logical_expressions(self):
        # logical expression check test

        with self.assertRaises(AssertionError):
            InputArmor.advanced_check(rabbit="1==1")
            InputArmor.advanced_check(rabbit="or True is True")
            InputArmor.advanced_check(rabbit="1 > 0")

    def test_advanced_check_keywords(self):
        # keywords check

        with self.assertRaises(AssertionError):
            InputArmor.advanced_check(rabbit="while True", check_for_keywords=True)
            InputArmor.advanced_check(rabbit="or true", check_for_keywords=True)

    def test_advanced_check_punctuation_symbols(self):
        # punctuation symbols check

        with self.assertRaises(AssertionError):
            InputArmor.advanced_check(rabbit="-- ls", check_for_punctuation_symbols=True)
            InputArmor.advanced_check(rabbit="#!", check_for_punctuation_symbols=True)

    def test_for_possible_values_without_iterable(self):
        # failed item persistence check without iterable given

        with self.assertRaises(TypeError):
            InputArmor.advanced_check(rabbit='apple', check_for_undefined_value=True)

    def test_for_possible_values(self):
        # if item persistence check
        self.assertIsNone(InputArmor.advanced_check(rabbit='apple',
                                                    check_for_undefined_value=True,
                                                    possible_values=self.possible_values))
        with self.assertRaises(AssertionError):
            InputArmor.advanced_check(rabbit='helicopter',
                                      check_for_undefined_value=True,
                                      possible_values=self.possible_values)

    # ---- sql_injection_check
    def test_sql_injection_soft_check(self):
        # Test case for sql_injection_check method in soft check mode
        self.assertIsNone(InputArmor.sql_injection_check("update string", check_level=1))

        with self.assertRaises(AssertionError):
            InputArmor.sql_injection_check(rabbit="drop table", check_level=1)
            InputArmor.sql_injection_check(rabbit="execute", check_level=1)
            InputArmor.sql_injection_check(rabbit="delete user", check_level=1)

    def test_sql_injection_hard_check(self):
        # Test case for sql_injection_check method in soft check mode
        self.assertIsNone(InputArmor.sql_injection_check("valid_sql_string", check_level=2))

        with self.assertRaises(AssertionError):
            self.assertIsNone(InputArmor.sql_injection_check("update string", check_level=2))

    def test_html_injection_soft_check(self):
        with self.assertRaises(AssertionError):
            InputArmor.html_injection_check(rabbit="getElementById", check_level=1)
            InputArmor.html_injection_check(rabbit="innerHTML", check_level=1)

    def test_html_injection_hard_check(self):

        with self.assertRaises(AssertionError):
            self.assertIsNone(InputArmor.html_injection_check("localStorage", check_level=2))
            self.assertIsNone(InputArmor.html_injection_check("static", check_level=2))


if __name__ == '__main__':
    unittest.main()
