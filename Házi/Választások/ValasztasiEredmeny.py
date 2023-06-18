class ValasztasiEredmeny:
    # 5 19 Ablak Antal -
    _kerulet: int
    _szavazatok: int
    _vnev: str
    _knev: str
    _part_jel: str

    @property
    def nev(self) -> str:
        return f'{self._vnev} {self._knev}'

    @property
    def szavazatok(self) -> int:
        return self._szavazatok

    @property
    def part(self) -> str:
        partok_szotar: dict[str, str] = {
            'GYEP': 'Gyümölcsevők pártja',
            'HEP': 'Húsevők párjtja',
            'TISZ': 'Tejívók szövetsége',
            'ZEP': 'Zöldségevők párja',
            '-': 'Független jelöltek'}
        return partok_szotar[self._part_jel]

    @property
    def partjel(self) -> str:
        # if self._part_jel == '-':
        #     return 'független'
        # else:
        #     return self._part_jel
        return 'független' if self._part_jel == '-' else self._part_jel

    @property
    def kerulet(self) -> int:
        return self._kerulet

    @kerulet.setter
    def kerulet(self, value: int) -> None:
        if value > 0 and value < 24:
            self._kerulet = value
        else:
            raise ValueError("A kerület 1-23 között lehet!")

    def __init__(self, sor: str) -> None:
        kerulet, szavazatok, vnev, knev, pjel = sor.split(' ')
        # self._kerulet = int(kerulet)  # így nincs ellenőrzés
        self.kerulet = int(kerulet)  # így a setter ellenőrzi az értéket
        self._szavazatok = int(szavazatok)
        self._vnev = vnev
        self._knev = knev
        self._part_jel = pjel
