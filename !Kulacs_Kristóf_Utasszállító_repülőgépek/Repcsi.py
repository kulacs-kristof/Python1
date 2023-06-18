class Repcsi(object):
    # típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv
    _típus: str
    _év: int
    _utas: str
    _személyzet: str
    _sebesség: int
    _felszállótömeg: int
    _fesztáv: float

    # 2. feladat Python módra:
    @property
    def sebesség_kategória(self) -> str:
        if self._sebesség < 500:
            return 'Alacsony sebességű'
        elif self._sebesség < 1000:
            return 'Szubszonikus'
        elif self._sebesség < 1200:
            return 'Transzszonikus'
        else:
            return 'Szuperszonikus'

    @property
    def típus(self) -> str:
        return self._típus

    @property
    def max_utas(self) -> int:
        return int(self._utas.split('-')[-1])

    @property
    def adatok(self) -> str:
        vissza: str = f'\tTípus: {self._típus}\n'
        vissza += f'\tElső felszállás: {self._év}\n'
        vissza += f'\tUtasok száma: {self._utas}\n'
        vissza += f'\tSzemélyzet: {self._személyzet}\n'
        vissza += f'\tUtazósebesség: {self._sebesség}\n'
        return vissza

    def __init__(self, sor: str):
        t, é, u, sz, s, ftömeg, ftáv = sor.split(';')
        self._típus = t
        self._év = int(é)
        self._utas = u
        self._személyzet = sz
        self._sebesség = int(s)
        self._felszállótömeg = int(ftömeg)
        self._fesztáv = float(ftáv.replace(',', '.'))
