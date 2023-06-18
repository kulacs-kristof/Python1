from random import randint
from random import *


def main() -> None:
    # Töltsünk fel egy listát véletlenszerűen 2jegyű számokkal majd határozzuk meg a prímszámok átlagát
    # A prímszámok kereséséhez használjunk függvényt

    lista = []
    primek = []
    for _ in range(1, 100):
        lista.append(randint(10, 99))

    for szam in lista:
        if fuggveny(szam):
            primek.append(szam)

    print(f"Számok: {lista}")
    print(f"Prímszámok: {primek}")
    if len(primek) == 0:
        print("Nincs prímszám")
    else:
        print(f"Prímszámok átlaga: {round(sum(primek) / len(primek), 2)}")


def fuggveny(szam: int) -> bool:
    for i in range(2, szam):
        if szam % i == 0:
            return False
    return True


if __name__ == "__main__":
    lista = sample(range(10, 99), 50)
    print(lista)
