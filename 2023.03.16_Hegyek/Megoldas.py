from Epulet import *


class Megoldas:
    Epuletek = []

    def __init__(self) -> None:
        self.FajlOlvasas("legmagasabb.txt")

    def FajlOlvasas(self, fajlnev):
        f = open(fajlnev, "r", encoding="utf-8")
        f.readline()
        for sor in f:
            self.Epuletek.append(Epulet(sor))
        f.close()

    def GetSzam(self):
        return len(self.Epuletek)

    def SumEmeletek(self):
        ossz = 0
        for e in self.Epuletek:
            ossz += e.Emelet
        return ossz

    def LegmagasabbEpulet(self):
        max = self.Epuletek[0]
        for e in self.Epuletek:
            if e.Magassag > max.Magassag:
                max = e
        return max

    def OlaszKeres(self):
        for e in self.Epuletek:
            if e.Orszag == "Olaszország":
                return True
        return False
