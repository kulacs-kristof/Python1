from eredmeny import *


class Megoldas:
    eredmenyek = []

    def __init__(self):
        self.fileBeolvas("fob2016.txt")

    def fileBeolvas(self, file):
        with open(file, "r", encoding="utf-8") as f:
            for sor in f:
                self.eredmenyek.append(Eredmeny(sor))
        f.close()

    def getVersenyzoSzama(self):
        return len(self.eredmenyek)

    def getNoiVersenyzoSzazalek(self):
        n = 0
        for i in self.eredmenyek:
            if i.Kategoria == "Noi":
                n += 1
        return round(n / len(self.eredmenyek) * 100, 2)

    def getNoiBajnok(self):
        nokLista = []
        for eredmeny in self.eredmenyek:
            if eredmeny.Kategoria == "Noi":
                nokLista.append(eredmeny)

        maxPontszam = nokLista[0]
        for eredmeny in nokLista[:1]:
            if eredmeny.osszPontszam() > maxPontszam.osszPontszam():
                maxPontszam = eredmeny.osszPontszam()

        return maxPontszam

    def StatKeszit(self):
        stat = {}
        for eredmeny in self.eredmenyek:
            if eredmeny.Egyesulet != "n.a":
                if eredmeny.Egyesulet not in stat.keys():
                    stat[eredmeny.Egyesulet] = 1
                else:
                    stat[eredmeny.Egyesulet] += 1

        return stat
