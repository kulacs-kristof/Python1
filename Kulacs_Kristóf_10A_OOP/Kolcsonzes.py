class Kolcsonzes:
    nev: str
    azon: str
    ora: int
    perc: int
    vissz_o: int
    vissz_p: int

    @property
    def vissza_percekben_kifejezve(self) -> int:
        return self.vissz_o * 60 + self.vissza_percekben_kifejezve

    def __init__(self, sor: str):
        nev, azo, o, p, vo, vp = sor.split(';')
        self.nev = nev
        self.azon = azo
        self.ora = int(o)
        self.perc = int(p)
        self.vissz_o = int(vo)
        self.vissz_p = int(vp)
