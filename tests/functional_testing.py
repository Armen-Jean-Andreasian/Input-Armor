import unittest
from main import InputArmor


class TestInputArmor(unittest.TestCase):
    valid_string = "valid_string"

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
            InputArmor.advanced_check("й, ў, ї")

    def test_sql_injection_check(self):
        # Test case for sql_injection_check method
        # Test with valid string, all checks pass
        self.assertIsNone(InputArmor.sql_injection_check("valid_sql_string", check_level=1))

        # Add more test cases for other scenarios

    def test_html_injection_check(self):
        # Test case for html_injection_check method
        # Test with valid string, all checks pass
        self.assertIsNone(InputArmor.html_injection_check("valid_html_string", check_level=1))

        # Add more test cases for other scenarios


if __name__ == '__main__':
    unittest.main()
