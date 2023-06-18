import random


def main() -> None:
    # Töltsünk fel egy listát x db kétjegyű páratlan számmal véletlenszerűen
    # Döntsük el, hogy a listában található-e prím szám
    # A keresést szakítsuk meg, ha találtunk prímet

    szamok: list[int] = []
    x: int = 3
    while len(szamok) < x:
        szam = random.randint(11, 51)
        if szam % 2 == 1:
            szamok.append(szam)
    print(szamok)
    for (i, szam) in enumerate(szamok):
        if prime(szam):
            print(f"A {i}. szám prím: {szam}")
            break
    else:
        print("Nincs prím szám a listában")


def prime(n: int) -> bool:
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


if __name__ == "__main__":
    main()
