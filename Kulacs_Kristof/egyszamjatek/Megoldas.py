from Jatekos import Jatekos


class Megoldas:
    _jatekosok: list[Jatekos] = []

    @property
    def jatekosok_szama(self) -> int:
        return len(self._jatekosok)

    @property
    def fordulok_szama(self) -> int:
        return self._jatekosok[0].tippek_szama

    @property
    def jatek_legnagyobb_tippje(self) -> int:
        # Megoldás max() fügvénnyel:
        # return max(jatekos.legnagyobb_tipp for jatekos in self._jatekosok)
        max_tipp: int = self._jatekosok[0].legnagyobb_tipp
        for jatekos in self._jatekosok[1:]:
            if jatekos.legnagyobb_tipp > max_tipp:
                max_tipp = jatekos.legnagyobb_tipp
        return max_tipp

    @property
    def volt_egyes_tipp(self) -> bool:
        volt_egyes: bool = False
        for jatekos in self._jatekosok:
            if jatekos.fordulok_tippje(1) == 1:
                volt_egyes = True
                break
        return volt_egyes

    def __init__(self, forras: str) -> None:
        self._jatekosok = []
        with open(forras, 'r', encoding='utf-8') as file:
            for sor in file.read().splitlines():
                self._jatekosok.append(Jatekos(sor))
