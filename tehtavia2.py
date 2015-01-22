import unittest
import sys
from io import StringIO

__unittest = True

"""
*
*
* Python-tehtäviä
*
* 2 - Lämmittelytehtäviä
*
* Täytä funktioiden määritelmät ohjeiden mukaan.
*
*
"""

"""
Täytä funktio suurin palauttamaan kolmesta numerosta suurin.
"""
def suurin(x,y,z):
    return 0


"""
Täytä funktio jarjestys(x,y,z) palauttamaan annetut numerot kasvavassa suuruusjärjestyksessä.
"""
def jarjestys(x,y,z):
    return 0


"""
Täytä funktio listansumma(lista) palauttamaan listan summa.
"""
def listansumma(lista):
    return 0























"""
*
*
*       Testiosio
* Älä muokkaa, ellet osaa.
*
*
"""
class TestSequenceFunctions(unittest.TestCase):

    @unittest.skipIf(suurin(1,2,3)==0, "täyttämätön funktio")
    def test_suurin(self):
        self.assertEqual(suurin(1,2,3) == 3)
        self.assertEqual(suurin(1,3,2) == 3)
        self.assertEqual(suurin(3,2,1) == 3)
        self.assertEqual(suurin(0,0,0) == 0,     "Mitä tehdä, jos kaikki argumentit ovat samoja?")
        self.assertEqual(suurin(-1,-2,-3) == -1, "Kuinka negatiiviset luvut käsitellään?")

    @unittest.skipIf(jarjestys(1,2,3)==0, "täyttämätön funktio")
    def test_jarjestys(self):
        self.assertEqual(jarjestys(1,2,3) == (1,2,3))
        self.assertEqual(jarjestys(1,3,2) == (1,2,3))
        self.assertEqual(jarjestys(3,2,1) == (1,2,3))
        self.assertEqual(jarjestys(0,0,0) == (0,0,0),       "Mitä tehdä, jos kaikki argumentit ovat samoja?")
        self.assertEqual(jarjestys(-1,-2,-3) == (-3,-2,-1), "Kuinka negatiiviset luvut käsitellään?")

    @unittest.skipIf(listansumma([1,2,3])==0, "täyttämätön funktio")
    def test_listansumma(self):
        self.assertEqual(listansumma([1,2,3]) == 6)
        self.assertEqual(listansumma([1]) == 1)
        self.assertEqual(listansumma([6,6,6]) == 18)
        self.assertEqual(listansumma([-1,1,-1,1]) == 0)
        self.assertEqual(listansumma([]) == 0, "entä jos lista on tyhjä?")


if __name__ == '__main__':
    print("*** Suoritetaan testit ***")
    unittest.main(verbosity=2,exit=False)
