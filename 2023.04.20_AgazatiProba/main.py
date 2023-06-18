from radio import radio

radiok = []


def fileOlvas(file):
    with open(file, "r", encoding="utf-8") as file:
        for line in file.read().splitlines()[1:]:
            radiok.append(radio(line))
    file.close()


def bejegyzesSzam(nev):
    bejegyzesekSzama = 0
    for e in radiok:
        if e.becenév == nev:
            bejegyzesekSzama += 1
    return bejegyzesekSzama


def LegtobbAdas():
    maxAdasok = [radiok[0]]
    for e in radiok[1:]:
        if e.adasok > maxAdasok[0].adasok:
            maxAdasok.clear()
            maxAdasok.append(e)
        elif e.adasok == maxAdasok[0].adasok:
            maxAdasok.append(e)

    return maxAdasok


def fileKiiras(filenév):
    with open(filenév, "w", encoding="utf-8") as file:
        file.write("Kezdes;Nev;AdasDb\n")
        for e in radiok:
            perc = e.ora * 60 + e.perc
            file.write(f"{perc};{e.becenév};{e.adasDB}\n")


fileOlvas("cb.txt")

# 2. feladat
print(f"3.2 feladat: Bejegyzések száma: {len(radiok)} db")

# 3. feladat
print(f"3.3 feladat: Sanyihoz tartozó bejegyzések: {bejegyzesSzam('Sanyi')} db")

# 4. feladat
print("3.4 feladat: A legtöbb adás:")
adasDB = LegtobbAdas()
for adas in adasDB:
    print(f"\tIdő: {adas.ora}:{adas.perc} Dabab:{adas.adasok} Név:{adas.becenév}")

# 5. feladat
fileKiiras("cb2.txt")
