def szamokÖsszege(lanc):
    osszeg = 0
    for karakter in lanc:
        if karakter.isnumeric():
            osszeg += int(karakter)
    return osszeg


def szavakSzama(lanc):
    return len(lanc.split(" "))


def szovegAtalakitas(lanc):
    return lanc.swapcase()


bemenet = "0"
while bemenet != "":
    bemenet = input("Adjon meg egy karakterlácot: ")
    if bemenet == "":
        break

    print(f"A karakterlánc számainak összege: {szamokÖsszege(bemenet)}")

    print(f"Szavak száma: {szavakSzama(bemenet)}")

    print(f"Átalakított karakterlánc: {szovegAtalakitas(bemenet)}")
