import unittest
from multiply_digit import multiply_digit


class BasicTestSuite(unittest.TestCase):

    def test_multiply_digit(self):
        self.assertEqual(multiply_digit(123045), ('120'))
        self.assertEqual(multiply_digit(-2035), ('-30'))
        self.assertEqual(multiply_digit(0), ('0'))


if __name__ == '__main__':
    unittest.main()
