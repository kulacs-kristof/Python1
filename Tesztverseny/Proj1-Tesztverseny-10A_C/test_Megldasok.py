import filecmp
from unittest import TestCase
from Megoldasok import Megoldasok


class TestMegoldas(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.megoldas1: Megoldasok = Megoldasok('valaszok.txt')

    def test_versenyzokszama(self):
        self.assertEqual(self.megoldas1.versenyzok_szama, 303)

    def test_valaszok(self):
        self.assertEqual(self.megoldas1.valaszok('AB123'), 'BXCDBBACACADBC')
        self.assertEqual(self.megoldas1.valaszok('AH97'), 'BCACDBDDBCBBCA')

    def test_megoldas(self):
        self.megoldas1.valaszok('AB123')
        self.assertEqual(self.megoldas1.megoldas, '+ +  +   +    ')

    def test_feladat_index(self):
        f5 = self.megoldas1.feladat_index(10)
        self.assertEqual(f5[0], 111)
        self.assertEqual(f5[1], 36.63)

    def test_fajl_kiiras(self):
        self.megoldas1.fájl_kiírás(self.megoldas1.versenyzok_pont_szama)
        self.assertTrue(filecmp.cmp('pontok.txt', 'pontokOH.txt', shallow=False))
