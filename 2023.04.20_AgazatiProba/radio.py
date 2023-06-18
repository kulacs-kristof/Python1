class radio:
    def __init__(self, sor):
        adatok = sor.split(";")
        self.ora = int(adatok[0])
        self.perc = int(adatok[1])
        self.adasDB = int(adatok[2])
        self.becenév = adatok[3]
