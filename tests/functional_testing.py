import unittest
from ..main import InputArmor


class TestInputArmor(unittest.TestCase):
    def test_advanced_check(self):
        # Test case for advanced_check method
        # Test with valid string, all checks pass
        self.assertIsNone(InputArmor.advanced_check("valid_string", check_encoding=True, check_length=True, fixed_length=10))

        # Test with invalid string type
        with self.assertRaises(TypeError):
            InputArmor.advanced_check(123)

        # Add more test cases for other scenarios

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