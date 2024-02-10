from checks import presence_check
import unittest


class BadLengthTest(unittest.TestCase):
    container_1 = [12, 'abvsd', True, 2j]
    container_2 = ["2", 'abvsd', "True", "2j"]

    value_1 = "12"
    value_2 = "13"
    value_3 = "true"
    value_4 = "2j"
    value_5 = "abvsd"

    def test_fail_1(self):
        with self.assertRaises(TypeError) as context:
            presence_check(rabbit=BadLengthTest.value_1, possible_values=BadLengthTest.container_1)

    def test_fail_2(self):
        with self.assertRaises(AssertionError) as context:
            presence_check(rabbit=BadLengthTest.value_2, possible_values=BadLengthTest.container_2)

    def test_fail_3(self):
        with self.assertRaises(AssertionError) as context:
            presence_check(rabbit=BadLengthTest.value_3, possible_values=BadLengthTest.container_2)

    def test_success_1(self):
        self.assertIsNone(presence_check(rabbit=BadLengthTest.value_4, possible_values=BadLengthTest.container_2))

    def test_success_2(self):
        self.assertIsNone(presence_check(rabbit=BadLengthTest.value_5, possible_values=BadLengthTest.container_2))



if __name__ == '__main__':
    unittest.main()
