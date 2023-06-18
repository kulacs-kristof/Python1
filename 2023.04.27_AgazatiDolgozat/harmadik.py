from eredmeny import eredmeny

eredmenyek = []


def fileBeolvas(fájl):
    with open(fájl, "r", encoding="utf-8") as file:
        for line in file.read().splitlines():
            eredmenyek.append(eredmeny(line))


def elitJuniorSzam():
    szam = 0
    for e in eredmenyek:
        if e.kategoria == "elit junior":
            szam += 1
    return szam


def atlageletkor():
    eletkor = 0
    for e in eredmenyek:
        eletkor += e.kor()

    return round(eletkor / len(eredmenyek), 1)


def kategoria(kat):
    rajtszamok = []

    for e in eredmenyek:
        if e.kategoria == kat:
            rajtszamok.append(e.rajtszam)

    return rajtszamok


def legjobbNo():
    legjobb = eredmenyek[0]
    for e in eredmenyek:
        if not e.isNo():
            continue
        if e.osszido() < legjobb.osszido():
            legjobb = e

    return legjobb.nev


fileBeolvas("Eredmenyek.txt")

print(f"2. feladat: A versenyt {len(eredmenyek)} versenyző fejezte be.")

print(f'3. feladat: Versenyzők száma az "elit junior" kategóriában: {elitJuniorSzam()} fő')

print(f"4. feladat: Átlagéletkor: {atlageletkor()} év.")

# 5.feladat
kategoriaInp = input("5. feladat: Kérek egy kategóriát: ")
kategoriak = kategoria(kategoriaInp)
print("\tRajtszam(ok): ", end="")
if len(kategoriak) == 0:
    print("Nincs ilyen kategória!", end="")
else:
    for e in kategoriak:
        print(e, end=" ")

# 6. feladat
print(f"\n6. feladat: A legjobb időt {legjobbNo()} érte el")
