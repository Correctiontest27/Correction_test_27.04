import unittest
from syracuse import syracuse

class BasicTestSuite(unittest.TestCase):

    def test_syracuse(self):
        """ test de la fonction syracuse """
        self.assertEqual(syracuse(7) , [22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(syracuse(10) , [5, 16, 8, 4, 2, 1])
        self.assertNotEqual(syracuse(10) , [6, 16, 8, 4, 2, 1])
        # self.assertRaises(syracuse("b"))





