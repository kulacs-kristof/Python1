class eredmeny:
    def ToMp(self, szam):
        szamok = szam.split(":")
        mp = 0
        mp += int(szamok[0]) * 3600
        mp += int(szamok[1]) * 60
        mp += int(szamok[2])
        return mp

    def __init__(self, sor) -> None:
        adatok = sor.split(";")
        self.nev = adatok[0]
        self.szuletes = int(adatok[1])
        self.rajtszam = int(adatok[2])
        self.nem = adatok[3]
        self.kategoria = adatok[4]

        self.uszasido = self.ToMp(adatok[5])
        self.elsoDepo = self.ToMp(adatok[6])
        self.kerekparozas = self.ToMp(adatok[7])
        self.masodikDepo = self.ToMp(adatok[8])
        self.futas = self.ToMp(adatok[9])

    def isNo(self):
        return self.nem == "n"

    def kor(self):
        return int(2014 - self.szuletes)

    def osszido(self):
        return self.uszasido + self.elsoDepo + self.kerekparozas + self.masodikDepo + self.futas
