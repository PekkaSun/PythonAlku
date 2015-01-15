"""
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.
"""

import unittest
import sys
from io import StringIO

__unittest = True

"""
*
*
* Python-tehtäviä
*
* 1 - Lämmittelytehtäviä
*
* Täytä funktioiden määritelmät ohjeiden mukaan.
*
*
"""


"""
Täytä funktio hello1() palauttamaan arvo "Hello, World!"
"""
def hello1():
    return "Hello, World!"

"""
Täytä funktio hello2() tulostamaan arvo "Hello, World!"
"""
def hello2():
    return 0
    
"""
Täytä funktio hello3() ottamaan nimi argumenttina ja tulostamaan
"Hello, (nimi)!"
Esim. hello3("Jaakko") -> "Hello, Jaakko!"
"""
def hello3(nimi):
    return 0
    
"""
Täytä funktio plus1() toteuttamaan plus1(x) = x+1
"""
def plus1(num):
    return 0

"""
Täytä funktio plus2() palauttamaan kahden argumenttinsa summan:
plus2(1, 2) -> 3
"""
def plus2(num1, num2):
    return 0

"""
Täytä funktio merkki() palauttamaan "Positiivinen" jos annettu luku on positiivinen
ja vastaavasti "Negatiivinen" jos luku on negatiivinen. Nollan tapauksessa palauta
"Nolla".
merkki(5)  -> "Positiivinen"
merkki(-1) -> "Negatiivinen"
merkki(0)  -> "Nolla"
"""
def merkki(x):
    return 0

"""
Täytä funktio tulo() palauttamaan kahden annetum luvun tulo.
tulo(2,3) -> 6
"""
def tulo(x, y):
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

    @unittest.skipIf(hello1()==0, "täyttämätön funktio")
    def test_hello1(self):
        self.assertEqual(hello1(),"Hello, World!",
                         'Palautettu arvo ei ole "Hello, World!"')
        
    @unittest.skipIf(hello2()==0, "täyttämätön funktio")
    def test_hello2(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            hello2()
            output = out.getvalue().strip()
            self.assertEqual(output, "Hello, World!",
                             'Tulostettu arvo ei ole "Hello, World!"')
        finally:
            sys.stdout = saved_stdout
            
    @unittest.skipIf(hello3("a")==0, "täyttämätön funktio")
    def test_hello3jaakko(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            hello3("Jaakko")
            output = out.getvalue().strip()
            self.assertEqual(output, "Hello, Jaakko!",
                             'Tulostettu arvo argumentilla "Jaakko" ei ollut "Hello, Jaakko!"')
        finally:
            sys.stdout = saved_stdout
            
    @unittest.skipIf(hello3("a")==0, "täyttämätön funktio")
    def test_hello3pekka(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            hello3("Pekka")
            output = out.getvalue().strip()
            self.assertEqual(output, "Hello, Pekka!",
                             'Tulostettu arvo argumentilla "Pekka" ei ollut "Hello, Jaakko!"')
        finally:
            sys.stdout = saved_stdout
            
    @unittest.skipIf(plus1(0)==0, "täyttämätön funktio")
    def test_plus1(self):
        self.assertEqual(plus1(0),1, "Nolla plus yksi on yksi.")
        self.assertEqual(plus1(-1),0, "(-1) + 1 = 0")
        self.assertEqual(plus1(1),2, "1 + 1 = 2")
        self.assertEqual(plus1(1000),1001, "1000 + 1 = 1001")
        self.assertEqual(plus1(-1001),-1000, "(-1001) + 1 = -1000")

    @unittest.skipIf(plus2(1,1)==0, "täyttämätön funktio")
    def test_plus2(self):
        self.assertEqual(plus2(0,0),0, "Nolla plus nolla on nolla.")
        self.assertEqual(plus2(-1,1),0, "(-1) + 1 = 0")
        self.assertEqual(plus2(1,-1),0, "1 + (-1) = 0")
        self.assertEqual(plus2(1,1),2, "1 + 1 = 2")
        self.assertEqual(plus2(0,1),1, "0 + 1 = 1")
        self.assertEqual(plus2(1000,1000),2000, "1000 + 1000 = 2000")
        self.assertEqual(plus2(-15000,5000),-10000, "-15000 + 5000 = -10000")

    @unittest.skipIf(merkki(1)==0, "täyttämätön funktio")
    def test_merkki(self):
        self.assertEqual(merkki(1),"Positiivinen", "Luku 1 on positiivinen.")
        self.assertEqual(merkki(10000),"Positiivinen", "Luku 10000 on positiivinen.")
        self.assertEqual(merkki(0.1),"Positiivinen", "Luku 0.1 on positiivinen.")
        self.assertEqual(merkki(0),"Nolla")
        self.assertEqual(merkki(-1),"Negatiivinen", "Luku -1 on negatiivinen.")
        self.assertEqual(merkki(-0.1),"Negatiivinen", "Luku -0.1 on negatiivinen.")
        self.assertEqual(merkki(-10000),"Negatiivinen", "Luku -10000 on negatiivinen.")

    @unittest.skipIf(tulo(1,1)==0, "täyttämätön funktio")
    def test_tulo(self):
        self.assertEqual(tulo(0,1), 0, "Nolla kertaa yksi on nolla.")
        self.assertEqual(tulo(1,1), 1, "1 * 1 = 1")
        self.assertEqual(tulo(1,-1), -1, "1 * (-1) = -1")
        self.assertEqual(tulo(0,1000456), 0, "0 * 1000456 = 0")
        self.assertEqual(tulo(2,3), 6, "2 * 3 = 6")
        self.assertEqual(tulo(-100,100), -10000, "(-100) * 100 = -10000")
        self.assertEqual(tulo(0.5,2), 1.0, "0.5 * 2 = 1.0")
        self.assertEqual(tulo(0.5,1), 0.5, "0.5 * 1 = 0.5")



if __name__ == '__main__':
    print("*** Suoritetaan testit ***")
    unittest.main(verbosity=2,exit=False)
