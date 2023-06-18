class Fogadasi_fordulo:

    def __init__(self, sor) -> None:
        adatok = sor.split(';')
        self.ev = int(adatok[0])
        self.het = int(adatok[1])
        self.fordulo = int(adatok[2])
        self.talalatok = int(adatok[3])
        self.nyeremeny = int(adatok[4])
        self.eredmenyek = str(adatok[5])