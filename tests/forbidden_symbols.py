from checks.punctuation_symbols import punctuation_symbols_check
import unittest


class BadLengthTest(unittest.TestCase):
    good_string = "asdklsajd1223"
    bad_string = "asdklsajd1223!"

    def test_success(self):
        self.assertIsNone(punctuation_symbols_check(BadLengthTest.good_string))

    def test_no_char(self):
        with self.assertRaises(AssertionError) as context:
            punctuation_symbols_check(BadLengthTest.bad_string)


if __name__ == '__main__':
    unittest.main()
