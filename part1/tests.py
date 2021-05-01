import unittest
from myfuncs import isalnum, tolower, lencmp, strcmp


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_isalnum(self):
        self.assertTrue(isalnum("32coucou"))
        self.assertTrue(isalnum("CouCo46819u"))
        self.assertTrue(isalnum("061498765432"))
        self.assertFalse(isalnum("061498765_(/!,)"))

    def test_tolower(self):
        self.assertEqual("emilie2000", tolower("EMILIE2000"))
        self.assertEqual("youpilavie", tolower("YouPiLaVie"))
	# test d'idempotence (involontaire, mais utile)
        self.assertEqual("test2...lamuerte!", tolower(tolower("teST2...laMueRte!")))0

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
	# tester le cas chaine2 plus longue, mais z plus grand que b
        self.assertEqual(strcmp("azc","abcd"),1)


if __name__ == '__main__':
    unittest.main()
