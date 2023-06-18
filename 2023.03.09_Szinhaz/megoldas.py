class megoldas:
    foglaltsagok = []
    kategoriak = []

    def fileOlvas(self, fajlnev, lista):
        f = open(fajlnev, 'r', encoding='utf-8')
        for sor in f:
            sorLista = []
            for elem in sor.strip():
                sorLista.append(elem)
            lista.append(sorLista)
        f.close()

    def getFoglaltsag(self, sor, szek):
        szek = int(szek) - 1
        sor = int(sor) - 1

        if self.foglaltsagok[sor][szek] == 'x':
            return True
        return False

    def getArany(self):
        xDb = 0
        osszes = len(self.foglaltsagok) * len(self.foglaltsagok[0])
        for sor in self.foglaltsagok:
            for szek in sor:
                if szek == 'x':
                    xDb += 1
        return xDb, round(xDb / osszes * 100, 0)

    def getKatLegtobb(self):
        stat = {}
        for sor in self.kategoriak:
            for szek in sor:
                if szek in stat.keys():
                    stat[szek] += 1
                else:
                    stat[szek] = 1
        maxi = 0
        maxKat = ''
        for key, value in stat.items():
            if value > maxi:
                maxi = value
                maxKat = key
        return maxKat

    def bevetelSzamol(self):
        ossz = 0
        for i in range(len(self.kategoriak)):
            for j in range(len(self.kategoriak[i])):
                if self.foglaltsagok[i][j] == 'x':
                    if self.kategoriak[i][j] != 5:
                        ossz += 6000 - int(self.kategoriak[i][j]) * 1000
                    else:
                        ossz += 1500
        return ossz

    def getUresHelyek(self):
        db = 0
        for i in range(len(self.kategoriak)):
            if self.foglaltsagok[i][0] == 'o' and self.foglaltsagok[i][1] == 'x':
                db += 1
            if self.foglaltsagok[i][-1] == 'o' and self.foglaltsagok[i][-2] == 'x':
                db += 1
            for j in range(1, len(self.foglaltsagok[i]) - 1):
                if self.foglaltsagok[i][j] == 'o' and self.foglaltsagok[i][j + 1] == 'x' and self.foglaltsagok[i][j - 1] == 'x':
                    db += 1
        return db

    def __init__(self) -> None:
        self.fileOlvas('foglaltsag.txt', self.foglaltsagok)
        self.fileOlvas('kategoria.txt', self.kategoriak)
