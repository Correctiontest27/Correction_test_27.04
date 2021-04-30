import unittest
from three_words import three_words, split1


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


if __name__ == '__main__':
    unittest.main()
