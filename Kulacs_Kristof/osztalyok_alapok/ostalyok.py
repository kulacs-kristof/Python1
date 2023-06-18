class Sikidom():
    # mezők (adattagok, protected láthatósági szintet a pythonban az "_" karakter jelöli)
    _kerület: float  # tárolás m-ben
    _terület: float  # tárolás m2-ben
    _mertekegyseg: str  # jellemzők a méreteket milyen mértékegységben adják meg

    # jellemzők
    # olvasható jellemző
    @property
    def kerület(self) -> float:
        if self._mertekegyseg == "miliméter":
            return self._kerület * 1000
        elif self._mertekegyseg == "centiméter":
            return self._kerület * 100
        elif self._mertekegyseg == "méter":
            return self._kerület
        else:
            return -1

    # írható/olvasható jellemző
    @property
    def terület(self) -> float:
        if self._mertekegyseg == "miliméter":
            return self._terület * 100000
        elif self._mertekegyseg == "centiméter":
            return self._terület * 10000
        elif self._mertekegyseg == "méter":
            return self._terület
        else:
            return -1

    @terület.setter
    def terület(self, value: float):
        if value > 0:
            self._terület = value

    # osztály konstruktora

    def __init__(self, kerület: float, terület: float, mertekegyseg: str):
        self._kerület = kerület
        self._terület = terület
        self._mertekegyseg = mertekegyseg


class Téglalap:
    _a: float
    _b: float

    @property
    def terület(self) -> float:
        return self._a * self._b

    @property
    def kerület(self) -> float:
        return 2 * (self._a + self._b)

    # public metódus
    def növel(self, delta: float) -> None:
        if delta > 0:
            self._a += delta
            self._b += delta

    def __init__(self, a: float, b: float):
        self._a = a
        self._b = b


def sikidom() -> None:
    # sikidom osztály példányosítása
    s1: Sikidom = Sikidom(3.5, 8.7, "centiméter")
    print(f'Kerület: {s1.kerület}')
    print(f'Terület: {s1.terület}')
    s1.terület = -12.45
    print(f'Terület: {s1.terület}')
    s1.terület = 12.45
    print(f'Terület: {s1.terület}')
    print("téglalap osztályok példányosítása")
    t1: Téglalap = Téglalap(10, 20)
    t2: Téglalap = Téglalap(2.5, 30)
    print(f't1: terület: {t1.terület}, kerület: {t1.kerület}')
    print(f't2: terület: {t2.terület}, kerület: {t2.kerület}')
    t1.növel(0.1)
    print(f't1: terület: {t1.terület}, kerület: {t1.kerület}')


if __name__ == "__main__":
    sikidom()
