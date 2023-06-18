from unittest import TestCase
from Megoldas import Megoldas


class TestMegoldas(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mo1: Megoldas = Megoldas('szavazatok.txt')

    def test_név(self) -> None:
        self.assertEqual(self.mo1.kepviselok_szama, 40)

    def test_képviselő_keresése(self) -> None:
        self.assertEqual(self.mo1.kepviselo_keresese('Ablak Antal'), '\tAz illető 19 szavazatot kapott.')
        self.assertEqual(self.mo1.kepviselo_keresese('Szabó János'), '\tIlyen nevű képviselőjelölt nem szerepel a nyilvántartásban!')

    def test_résztvevők_száma(self) -> None:
        self.assertEqual(self.mo1.resztvevok_szama, 4713)

    def test_résztvevők_százaléka(self) -> None:
        self.assertEqual(self.mo1.resztvevok_szazaleka, 38.17739975698664)

    def test_szavazatok_statisztika(self) -> None:
        self.assertEqual(self.mo1.szavazatok_stat, '\tFüggetlen jelöltek= 17.53%\n\tGyümölcsevők pártja= 16.36%\n\tZöldségevők párja= 20.03%\n\tHúsevők párjtja= 24.59%\n\tTejívók szövetsége= 21.49%\n')

    def test_győztes_képviselők(self) -> None:
        self.assertEqual(self.mo1.gyoztes_kepviselok, '\tJoghurt Jakab - TISZ\n\tNarancs Edmond - GYEP\n\tVadas Marcell - HEP\n')
