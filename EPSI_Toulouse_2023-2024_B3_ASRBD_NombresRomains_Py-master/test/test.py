import unittest
import parameterized.parameterized

from ConvertisseurNombresRomains import ConvertisseurNombresRomains


class NombresRomainsTest(unittest.TestCase):

    @parameterized.parameterized.expand([
        [1],
        [2],
    ])
    def test_unite(self, nombre_arabe):
        # ETANT DONNE le chiffre <nombre_arabe>
        # QUAND on le convertit en nombres romains
        nombre_romain = ConvertisseurNombresRomains.convertir(nombre_arabe)

        # ALORS on obtient "I" répété <nombre_arabe> fois
        attendu = "I" * nombre_arabe
        self.assertEqual(attendu, nombre_romain)
