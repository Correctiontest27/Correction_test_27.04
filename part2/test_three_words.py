import unittest
import sys
# bricolage pour ignorer les problemes d'import
# a ne pas utiliser en pratique (risque de masquer des erreurs)

from three_words import three_words

class BasicTestSuite(unittest.TestCase):

    def test_three_words(self):
        self.assertFalse(three_words("abc abv"))
        self.assertTrue(three_words("abc abv asd"))
        self.assertFalse(three_words(""))
        # commenté ce test pour permettre de montrer des versions alternatives (en restant dans les specs de l'énoncé)
        #self.assertTrue(three_words(["abc", "abv", "asdasd", "qwdsade"]))

        # pourquoi on passe par une affectation?
        # c'est utile uniquement  si le calcul est très long
        # sinon plus simple de faire :
        # self.assertIsInstance(three_words('asd avf 123123asd'), bool)
        # self.assertFalse(three_words('asd avf 123123asd'))
        x = three_words('asd avf 123123asd')
        self.assertIsInstance(x, bool)
        self.assertFalse(x)

    # pas une bonne pratique : si la fonction n'est pas imposée par la spec du problème 
    # alors la placer dans les unittest du projet impose aux autres devs de passer par la même fonction
    # donc on va bricoler un peu pour créer des tests optionnels (uniquement si elle existe)
    def test_split1(self):
        try:
            from three_words import split1
        except ImportError:
            raise unittest.SkipTest("Optional function three_words.split1 skipped")
        self.assertEqual(split1('hi my name is jeef'), ['hi', 'my', 'name', 'is', 'jeef'])
        self.assertEqual(split1(''), [])
        


if __name__ == '__main__':
    unittest.main()
