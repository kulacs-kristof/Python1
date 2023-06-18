from unittest import TestCase
from Valaszok import Valaszok


class testValaszok(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valaszok1: Valaszok = Valaszok('AB123 BXCDBBACACADBC')
        cls.valaszok2: Valaszok = Valaszok('AH97 BCACDBDDBCBBCA')
        cls.valaszok3: Valaszok = Valaszok('ZZ240 ABBCDADDCACDDD')
        cls.valaszok4: Valaszok = Valaszok('TC757 ABCACBBBDDBABA')
        cls.valaszok5: Valaszok = Valaszok('KN731 CAABDDBCCBDDAC')

    def test_azonosító(self):
        self.assertEqual(self.valaszok1.azonosito, 'AB123')
        self.assertEqual(self.valaszok2.azonosito, 'AH97')
        self.assertEqual(self.valaszok3.azonosito, 'ZZ240')
        self.assertEqual(self.valaszok4.azonosito, 'TC757')
        self.assertEqual(self.valaszok5.azonosito, 'KN731')

    def test_válaszok(self):
        self.assertEqual(self.valaszok1.valaszok, 'BXCDBBACACADBC')
        self.assertEqual(self.valaszok2.valaszok, 'BCACDBDDBCBBCA')
        self.assertEqual(self.valaszok3.valaszok, 'ABBCDADDCACDDD')
        self.assertEqual(self.valaszok4.valaszok, 'ABCACBBBDDBABA')
        self.assertEqual(self.valaszok5.valaszok, 'CAABDDBCCBDDAC')
