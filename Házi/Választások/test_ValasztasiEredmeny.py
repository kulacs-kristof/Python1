from unittest import TestCase
from ValasztasiEredmeny import ValasztasiEredmeny


class TestValasztasiEredmeny(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.eredmeny1: ValasztasiEredmeny = ValasztasiEredmeny('5 19 Ablak Antal -')
        cls.eredmeny2: ValasztasiEredmeny = ValasztasiEredmeny('1 120 Alma Dalma GYEP')

    def test_név(self) -> None:
        self.assertEqual(self.eredmeny1.nev, 'Ablak Antal')
        self.assertEqual(self.eredmeny2.nev, 'Alma Dalma')

    def test_szavazatok_száma(self) -> None:
        self.assertEqual(self.eredmeny1.szavazatok, 19)
        self.assertEqual(self.eredmeny2.szavazatok, 120)

    def test_párt(self) -> None:
        self.assertEqual(self.eredmeny1.part, 'Független jelöltek')
        self.assertEqual(self.eredmeny2.part, 'Gyümölcsevők pártja')

    def test_pártjel(self) -> None:
        self.assertEqual(self.eredmeny1.partjel, 'független')
        self.assertEqual(self.eredmeny2.partjel, 'GYEP')

    def test_kerület(self) -> None:
        self.assertEqual(self.eredmeny1.kerulet, 5)
        self.assertEqual(self.eredmeny2.kerulet, 1)

    def test_kerület_exception(self) -> None:
        self.assertRaises(ValueError, ValasztasiEredmeny, '91 44 Szabó János HEP')
        # self.assertRaisesRegexp('alma', ValasztasiEredmeny, '91 44 Szabó János HEP')
