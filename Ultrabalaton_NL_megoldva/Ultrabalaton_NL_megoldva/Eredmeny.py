class Eredmeny:
    # Versenyzo;Rajtszam;Kategoria;Versenyido;TavSzazalek
    név: str
    rajtszám: int
    kategória: str
    idő: str
    táv_százalék: int

    @property
    def őNő(self):
        return self.kategória == 'Noi'

    @property
    def táv_teljesítve(self):
        return self.táv_százalék == 100

    @property
    def név_hossza(self) -> int:
        return len(self.név)

    @property
    def idő_órában(self) -> float:
        óra, perc, mp = self.idő.split(':')
        return float(óra) + float(perc) / 60 + float(mp) / 3600

    def __init__(self, sor: str):
        név, rsz, kat, idő, tsz = sor.split(';')
        self.név = név
        self.rajtszám = int(rsz)
        self.kategória = kat
        self.idő = idő
        self.táv_százalék = int(tsz)
