from checks.length import length_check
import unittest


class BadLengthTest(unittest.TestCase):
    normal_string = "asdklsajd"
    no_char_string = "         "
    no_len_string = ""

    def test_success(self):
        self.assertIsNone(length_check(BadLengthTest.normal_string))

    def test_no_char(self):
        with self.assertRaises(AssertionError) as context:
            length_check(BadLengthTest.no_char_string)

    def test_empty_string(self):
        with self.assertRaises(AssertionError) as context:
            length_check(BadLengthTest.no_len_string)


if __name__ == '__main__':
    unittest.main()
