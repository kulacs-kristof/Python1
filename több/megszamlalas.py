import random
import time


def main() -> None:
    print("Megszámlálás programozási feltételei")
    szamok: list[int] = []
    for _ in range(random.randint(10, 15)):
        szamok.append(random.randint(10, 99))
    print(szamok)
    # Megoldás 1
    for (i, szam) in enumerate(szamok):
        if i % 2 == 0 and szam % 2 == 0:
            # print(f"A(z) {i}. {szam}.")
            pass

    # Megoldás 2
    for i in range(0, len(szamok), 2):
        if szamok[i] % 2 == 0:
            # print(f"A(z) {i}. {szamok[i]}.")
            pass

    # Megoldás 3
    for szam in szamok[::2]:
        if szam % 2 == 0:
            # print(szam)
            pass

    # Halmazban lévő páratlan számok darabszáma
    szamok_halmaz: list[int] = []
    utkozeseklista = []
    for _ in range(1000):
        szamok_halmaz.clear()
        utkozesek: int = 0
        while len(szamok_halmaz) < 80:
            szám = random.randint(10, 99)
            if szám not in szamok_halmaz:
                szamok_halmaz.append(szám)
            else:
                utkozesek += 1
        utkozeseklista.append(utkozesek)
    print(f"Utközések átlaga: {int(sum(utkozeseklista) / len(utkozeseklista))}")
    print(szamok_halmaz)
    db: int = 0
    for szam in szamok_halmaz:
        if szam % 2 == 1:
            db += 1
    print(f"Páratlan számok darabszáma: {db}")


if __name__ == "__main__":
    main()
