class Epulet:
    def __init__(self, sor):
        adatok = sor.strip().split(';')
        self.Nev = adatok[0]
        self.Varos = adatok[1]
        self.Orszag = adatok[2]
        self.Magassag = float(adatok[3].replace(',', '.'))
        self.Emelet = int(adatok[4])
        self.Epult = int(adatok[5])
