import unittest
from valid_password import valid_password


class BasicTestSuite(unittest.TestCase):

    def test_valid_password(self):
        assert False == valid_password("abcabd")
        assert False == valid_password("ajdueofd")
        assert False == valid_password("alekfkn?uuzd")
        assert False == valid_password("alekfknuuzd")
        assert False == valid_password("")
        assert False == valid_password("oianjdsj?")
        assert True == valid_password("1mmmmmmmmmm!")
        assert True == valid_password("1!@jdjsjdsjdsjdjsdjsdj")
        assert False == valid_password("535353535353535!")


if __name__ == '__main__':
    unittest.main()
