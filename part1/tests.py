import unittest
from myfuncs import isalnum, tolower, lencmp, strcmp


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_isalnum(self):
        assert True == isalnum("32coucou")
        assert True == isalnum("CouCo46819u")
        assert True == isalnum("061498765432")
        assert False == isalnum("061498765_(/!,)")

    def test_tolower(self):
        assert "emilie2000" == tolower("EMILIE2000")
        assert "youpilavie" == tolower("YouPiLaVie")
        assert "test2...lamuerte!" == tolower(tolower("teST2...laMueRte!"))

    def test_lencmp(self):
        self.assertEqual(lencmp("a", "b"), 0)
        self.assertEqual(lencmp("aa", "z"), 1)
        self.assertEqual(lencmp("z", "aa"), -1)

    def test_strcmp(self):
        self.assertEqual(strcmp("B", "abcd"), 1)
        self.assertEqual(strcmp("abc", "abcd"), -1)
        self.assertEqual(strcmp("z", "ysdkqljgh"), 1)
        self.assertEqual(strcmp("g", "tabc"), -1)
        self.assertEqual(strcmp("abc", "abc"), 0)
        self.assertEqual(strcmp("abcd", "abc"), 1)
	
        self.assertEqual(strcmp("azc","abcd"),1)


if __name__ == '__main__':
    unittest.main()
