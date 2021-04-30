import unittest
from fizzbuzz import fizzbuzz


class BasicTestSuite(unittest.TestCase):

    def Test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'Fizz Buzz')
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz(5), 'Buzz')
        self.assertEqual(fizzbuzz(6), 'Fizz')
        self.assertEqual(fizzbuzz(10), 'Buzz')
        self.assertEqual(fizzbuzz(30), 'Fizz Buzz')


if __name__ == '__main__':
    unittest.main()
