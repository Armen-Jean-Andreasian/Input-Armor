import unittest
from sql_checks import SqlInjectionCheck


class TestSqlInjectionCheck(unittest.TestCase):
    def test_malicious_string(self):
        malicious_string = "DROP TABLE users"
        with self.assertRaises(AssertionError):
            SqlInjectionCheck.run(malicious_string)

    def test_save_string(self):
        save_string = 'MyPassword123'
        self.assertIsNone(SqlInjectionCheck.run(save_string))


if __name__ == '__main__':
    unittest.main()
