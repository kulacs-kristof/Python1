# Függvény: Azonosítóval ellátott, jól specifikált feladatit ellátó utasítások csoportja
# Függvényt használat előtt definiálni kell
# Függvény definíció általános alakja
# def fuggveny_neve(paraméterek) -> visszatérési érték:
# A törzs jelölése indentálással történik
# Tetszőleg szám utasítással kódoljuk a függvény feladatait
# Legalább egy return utasítás után meghatározható a visszatérési érték
# kivétel: nincs return, ha a viszatérési érték None ("void")

import random
from time import sleep
# Készítsünk fuggvényt 3 szám összeadására

'''
def osszead(a: int, b: int, c: int) -> int:
    return a + b + c
'''

'''
def tokeletes(n: int) -> bool:
    osszeg = 0
    for x in range(1, n):
        if n % x == 0:
            osszeg += x
        if osszeg > n:
            return False
    return osszeg == n
'''

'''
def osztóharmonikus(n) -> bool:
    reciprokok = []

    for x in range(1, n + 1):
        if n % x == 0:
            reciprokok.append(round(1 / x, n))

    szam = len(reciprokok)
    print(szam)
    szam2 = 0

    for ertek in reciprokok:
        szam2 += ertek

    if (szam / szam2).is_integer():
        return True
    else:
        return False
'''


def osztóharmonikus(n: int) -> bool:
    if n % 2 != 0:
        return False
    osztóösszeg: float = 0
    osztószám: int = 0
    for x in range(1, n + 1):
        if n % x == 0:
            osztószám += 1
            osztóösszeg += 1 / x
    return round(osztószám / osztóösszeg, 4).is_integer()


def main() -> None:
    for x in range(1, 10000):
        if osztóharmonikus(x):
            print(x)


'''
def prime(n: int) -> bool:
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
'''

if __name__ == "__main__":
    main()
