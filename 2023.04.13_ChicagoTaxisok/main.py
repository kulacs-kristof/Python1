from Fuvar import Fuvar
fuvarok = []


def fileOlvasas(fileNév):
    with open(fileNév, "r", encoding="utf-8") as file:
        for sor in file.read().splitlines()[1:]:
            fuvarok.append(Fuvar(sor))
    file.close()


def osszFuvarSzam():
    return len(fuvarok)


def taxiInfo(taxiID):
    bevetel = 0
    fuvarokSzama = 0
    for e in fuvarok:
        if e.azonosito == taxiID:
            bevetel += e.viteldij + e.borravalo
            fuvarokSzama += 1
    return bevetel, fuvarokSzama


def fizetesiModokStat():
    tipusok = {}
    # Adatok kiszedése
    for e in fuvarok:
        if e.fizetesmod in tipusok:
            tipusok[e.fizetesmod] += 1
        else:
            tipusok[e.fizetesmod] = 1

    # Kiíras formázása
    szoveg = ""
    for key, item in tipusok.items():
        szoveg += f"\n\t{key}: {item} fuvar"
    return szoveg


def osszTavolsag():
    ossztav = 0
    for e in fuvarok:
        ossztav += merfoldToKm(e.tavolsag)

    return round(ossztav, 2)


def merfoldToKm(merfold):
    return merfold * 1.6


def leghosszabbFuvarInfok():
    leghosszabb = fuvarok[0]
    for e in fuvarok:
        if e.idotartam > leghosszabb.idotartam:
            leghosszabb = e

    return leghosszabb


def sort(x):
    return x.indulas


def FileKiiras():
    hibas_adatok = []
    for e in fuvarok:
        if (e.idotartam > 0 and e.viteldij > 0) and e.tavolsag == 0:
            hibas_adatok.append(e)

    with open("hibak.txt", "w", encoding="utf-8") as file:
        file.write("taxi_id;indulas;idotartam;tavolsag;viteldij;borravalo;fizetes_modja\n")
        for e in sorted(hibas_adatok, key=sort):
            file.write(e.adatokRaw() + "\n")
    file.close()


fileOlvasas("fuvar.csv")

print(f"3. feladat: {osszFuvarSzam()}")

taxiAdatok = taxiInfo(6185)
print(f"4. feladat: {taxiAdatok[1]} fuvar alatt: {taxiAdatok[0]}$")

print(f"5. feladat: {fizetesiModokStat()}")

print(f"6. feladat: {osszTavolsag()}km")

lF = leghosszabbFuvarInfok()
print("7. feladat: Leghosszabb fuvar:")
print(f"\tFuvar hossza: {lF.idotartam} másodperc")
print(f"\tTaxi azonosito: {lF.azonosito}")
print(f"\tMegtett táv: {lF.tavolsag} km")
print(f"\tViteldíj: {lF.viteldij}$")

FileKiiras()
print("8. feladat: hibak.txt")
