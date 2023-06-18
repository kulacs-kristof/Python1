class Jatekos:
    _nev: str
    _tippek: list[int] = []

    @property
    def tippek_szama(self) -> int:
        return len(self._tippek)

    @property
    def legnagyobb_tipp(self) -> int:
        # Megoldás max() fügvénnyel:
        # return max(self._tippek)
        max_tipp = self._tippek[0]
        for akt_tipp in self._tippek[1:]:
            if akt_tipp > max_tipp:
                max_tipp = akt_tipp
        return max_tipp

    def __init__(self, sor: str) -> None:
        self._tippek = []
        m: list[str] = sor.split(' ')
        self.nev = m[0]
        for tipp in m[1:]:
            self._tippek.append(int(tipp))

    def fordulok_tippje(self, fordulo_sorszama: int) -> int:
        return self._tippek[fordulo_sorszama - 1]
