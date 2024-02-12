import unittest
from input_armor import InputArmor


class TestSqlInjectionCheck(unittest.TestCase):
    def test_malicious_string(self):
        malicious_string = "DROP TABLE users"
        with self.assertRaises(AssertionError):
            InputArmor.sql_injection_check(malicious_string)

    def test_save_string(self):
        save_string = 'MyPassword123'
        self.assertIsNone(InputArmor.sql_injection_check(save_string))


if __name__ == '__main__':
    unittest.main()
