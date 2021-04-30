import unittest
from three_words import three_words, split1
from multiply_digit import digits
from fizzbuzz import fizzbuzz
from reverse_word import reverse_word


class BasicTestSuite(unittest.TestCase):
    def test_three_words(slef):
        assert False == three_words("abc abv")
        assert True == three_words("abc abv asd")
        assert False == three_words("")
        assert True == three_words(["abc", "abv", "asdasd", "qwdsade"])
        x = three_words('asd avf 123123asd')
        assert isinstance(x, bool)
        assert not x

    def test_split1(self):
        self.assertEqual(split1('hi my name is jeef'), ['hi', 'my', 'name', 'is', 'jeef'])
        self.assertEqual(split1(''), [])

    def digits_multi(self):
        self.assertEqual(digits(123045), ('120'))
        self.assertEqual(digits(-2035), ('-30'))
        self.assertEqual(digits(0), ('0'))

    def Test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'Fizz Buzz')
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz(5), 'Buzz')
        self.assertEqual(fizzbuzz(6), 'Fizz')
        self.assertEqual(fizzbuzz(10), 'Buzz')
        self.assertEqual(fizzbuzz(30), 'Fizz Buzz')

    def Test_reverse_word(self):
        self.assertEqual(reverse_word('abcdefg'), 'gfedcba')
        self.assertEqual(reverse_word('hello world'), 'dlrow olleh')
        self.assertEqual(reverse_word('asds22E0ssasq'), 'qsass0E22sdsa')


if __name__ == '__main__':
    unittest.main()
