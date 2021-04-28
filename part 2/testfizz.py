import unittest
from rendu_copy import Fizz_Buzz,Inverser


class BasicTestSuite(unittest.TestCase):
    def Test_Fizz_Buzz(slef):
        self.assertEqual(Fizz_Buzz(15),'Fizz buzz')
        self.assertEqual(Fizz_Buzz(3),'fizz')
        self.assertEqual(Fizz_Buzz(5),'buzz')
        self.assertEqual(Fizz_Buzz(6),'fizz')
        self.assertEqual(Fizz_Buzz(10),'buzz')
        self.assertEqual(Fizz_Buzz(30),'Fizz buzz')

    def Test_Inverser(self):
        self.assertEqual(Inverser('abcdefg'),'gfedcba')
        self.assertEqual(Inverser('hello world'),'dlrow olleh')
        self.assertEqual(Inverser('asds22E0ssasq'),'qsass0E22sdsa')


if __name__ == '__main__':
    unittest.main()