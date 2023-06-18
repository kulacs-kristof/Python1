class Eredmeny:
    # Versenyzo;Rajtszam;Kategoria;Versenyido;TavSzazalek
    nev: str
    rajtszam: int
    kategoria: str
    ido: str
    tav_szazalek: int

    @property
    def ono(self):
        return self.kategoria == 'Noi'

    @property
    def tav_teljesitve(self):
        return self.tav_szazalek == 100

    def __init__(self, sor: str):
        név, rsz, kat, idő, tsz = sor.split(';')
        self.nev = név
        self.rajtszam = int(rsz)
        self.kategoria = kat
        self.ido = idő
        self.tav_szazalek = int(tsz)

    def __str__(self):
