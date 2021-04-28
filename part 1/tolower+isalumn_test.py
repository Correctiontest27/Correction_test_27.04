from myfuncs import isalnum, tolower

import unittest

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


if __name__ == '__main__':
    unittest.main()