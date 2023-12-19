# test_convertisseur.py
import unittest
import subprocess
from ConvertisseurNombresRomains import ConvertisseurNombresRomains
from parameterized import parameterized

"""
@parameterized.parameterized.expand(
    [
        [1],
        [2],
        [3],
    ]
)
"""
class NombresRomainsTest(unittest.TestCase):
    def test_un(self):
        # ETANT DONNE le chiffre 1
        nombre_arabe = 1

        # QUAND on le convertit en nombres romains
        nombre_romain = ConvertisseurNombresRomains.convertir(nombre_arabe)

        # ALORS on obtient "I"
        self.assertEqual("I", nombre_romain)

        # If the test passes, push to GitHub
        self.git_push()

    def test_deux(self):
        # ETANT DONNE le chiffre 2
        nombre_arabe = 2

        # QUAND on le convertit en nombres romains
        nombre_romain = ConvertisseurNombresRomains.convertir(nombre_arabe)

        # ALORS on obtient "II"
        self.assertEqual("II", nombre_romain)

        # If the test passes, push to GitHub
        self.git_push()

    def test_trois(self):
        # ETANT DONNE le chiffre 3
        nombre_arabe = 3

        # QUAND on le convertit en nombres romains
        nombre_romain = ConvertisseurNombresRomains.convertir(nombre_arabe)

        # ALORS on obtient "III"
        self.assertEqual("III", nombre_romain)

        # If the test passes, push to GitHub
        self.git_push()

    def test_quatre(self):
        # ETANT DONNE le chiffre 4
        nombre_arabe = 4

        # QUAND on le convertit en nombres romains
        nombre_romain = ConvertisseurNombresRomains.convertir(nombre_arabe)

        # ALORS on obtient "IV"
        self.assertEqual("IV", nombre_romain)

        # If the test passes, push to GitHub
        self.git_push()

    def git_push(self):
        try:
            subprocess.run(["git", "add", "."])
            subprocess.run(
                ["git", "commit", "-m", "Automated commit after successful test"]
            )
            subprocess.run(["git", "push"])
        except Exception as e:
            print(f"Git push failed: {e}")


if __name__ == "__main__":
    unittest.main()
