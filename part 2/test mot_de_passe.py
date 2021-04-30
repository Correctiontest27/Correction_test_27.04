import unittest
from mot_de_passe import mot_de_passe
class BasicTestSuite(unittest.TestCase):

def test_mot_de_passe(self):
        assert False == mot_de_passe("abcabd")
        assert False == mot_de_passe("ajdueofd")
        assert False == mot_de_passe("alekfkn?uuzd")
        assert False == mot_de_passe("alekfknuuzd")
        assert False == mot_de_passe("")
        assert False == mot_de_passe("oianjdsj?")
        assert True == mot_de_passe("1mmmmmmmmmm!")
        assert True == mot_de_passe("1!@jdjsjdsjdsjdjsdjsdj")
        assert False == mot_de_passe("535353535353535!")
