class Eredmeny:
    def __init__(self, sor):
        self.pontszamok = []
        adatok = sor.strip().split(";")
        self.Nev = adatok[0]
        self.Kategoria = adatok[1]
        self.Egyesulet = adatok[2]
        for i in range(3, len(adatok)):
            self.pontszamok.append(int(adatok[i]))

    def osszPontszam(self):
        templist = sorted(self.pontszamok.copy())

        for i in range(0, 2):
            if templist[i] == 0:
                templist.remove(0)
            if templist[i] > 0:
                templist.append(10)

        return sum(templist)
