class Fuvar:

    def adatokRaw(self):
        return f"{self.azonosito};{self.indulas};{self.idotartam};{self.tavolsag};{self.viteldij};{self.borravalo};{self.fizetesmod}"

    def __init__(self, sor):
        adatok = sor.split(";")

        self.azonosito = int(adatok[0])
        self.indulas = str(adatok[1])
        self.idotartam = int(adatok[2])
        self.tavolsag = float(adatok[3].replace(",", "."))
        self.viteldij = float(adatok[4].replace(",", "."))
        self.borravalo = float(adatok[5].replace(",", "."))
        self.fizetesmod = str(adatok[6])
