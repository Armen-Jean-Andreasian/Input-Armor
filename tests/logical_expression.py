from input_armor.checks import logical_expression_check
import unittest


class ExpressionFoundTest(unittest.TestCase):
    bad_string_1 = "1==1"
    bad_string_2 = "2>1"
    bad_string_3 = "trueistrue"
    good_string = "asdklsajd1223"

    def test_success(self):
        self.assertIsNone(logical_expression_check(ExpressionFoundTest.good_string))

    def test_bad_1(self):
        with self.assertRaises(AssertionError) as context:
            logical_expression_check(ExpressionFoundTest.bad_string_1)

    def test_bad_2(self):
        with self.assertRaises(AssertionError) as context:
            logical_expression_check(ExpressionFoundTest.bad_string_2)

    def test_bad_3(self):
        with self.assertRaises(AssertionError) as context:
            logical_expression_check(ExpressionFoundTest.bad_string_3)


if __name__ == '__main__':
    unittest.main()
