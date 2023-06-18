from ValasztasiEredmeny import ValasztasiEredmeny


class Megoldas:
    _eredmenyek: list[ValasztasiEredmeny] = []

    @property
    def kepviselok_szama(self) -> int:
        return len(self._eredmenyek)

    @property
    def resztvevok_szama(self) -> int:
        szum: int = 0
        for e in self._eredmenyek:
            szum += e.szavazatok
        return szum

    @property
    def resztvevok_szazaleka(self) -> float:
        return self.resztvevok_szama / 12345 * 100

    def _szavazatok_szama(self, kepviselo_neve: str) -> int:
        for k in self._eredmenyek:
            if k.nev == kepviselo_neve:
                return k.szavazatok
        return -1

    @property
    def _stat(self) -> dict[str, int]:
        # elfogadható, de nem szép megooldás:
        # stat2: dict[str, int] = {
        #     'GYEP': 0,
        #     'HEP': 0,
        #     'TISZ': 0,
        #     'ZEP': 0,
        #     'független': 0}
        # for e in self._eredmenyek:
        #     stat2[e.part] += e.szavazatok

        stat: dict[str, int] = {}
        for e in self._eredmenyek:
            if e.part in stat:
                # ha már megtalálható a párt a szótárban:
                stat[e.part] += e.szavazatok  # növelés
            else:
                # ha még nincs a párt a azótárban
                stat[e.part] = e.szavazatok  # elhelyezés, kezdőérték beállítása
        return stat

    @property
    def _legtobb_szavazat(self) -> int:
        max_szavazat: int = -1
        for e in self._eredmenyek:
            if e.szavazatok > max_szavazat:
                max_szavazat = e.szavazatok
        return max_szavazat

    @property
    def gyoztes_kepviselok(self) -> str:
        vissza: str = ''
        for e in self._eredmenyek:
            if e.szavazatok == self._legtobb_szavazat:
                vissza += f'\t{e.nev} - {e.partjel}\n'
        return vissza

    @property
    def szavazatok_stat(self) -> str:
        vissza: str = ''
        for key, value in self._stat.items():
            vissza += f'\t{key}= {value / self.resztvevok_szama * 100:.2f}%\n'
        return vissza

    def kepviselo_keresese(self, kepviselo_neve: str) -> str:
        szavazatok_db: int = self._szavazatok_szama(kepviselo_neve)
        if szavazatok_db >= 0:
            return f'\tAz illető {szavazatok_db} szavazatot kapott.'
        else:
            return '\tIlyen nevű képviselőjelölt nem szerepel a nyilvántartásban!'

    def __init__(self, forras: str):
        with open(forras, 'r', encoding='utf-8') as file:
            # for sor in file.read().splitlines():
            #     self._eredmenyek.append(ValasztasiEredmeny(sor))
            for sor in file.read().splitlines():
                try:
                    self._eredmenyek.append(ValasztasiEredmeny(sor))
                except ValueError as ex:
                    print(ex)
