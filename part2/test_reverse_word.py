import unittest
from reverse_word import reverse_word


class BasicTestSuite(unittest.TestCase):

    def Test_reverse_word(self):
        self.assertEqual(reverse_word('abcdefg'), 'gfedcba')
        self.assertEqual(reverse_word('hello world'), 'dlrow olleh')
        self.assertEqual(reverse_word('asds22E0ssasq'), 'qsass0E22sdsa')


if __name__ == '__main__':
    unittest.main()
