import random
import math


def príme(x: int) -> bool:
    if x > 2 and x % 2 == 0 or x <= 1:
        return False
    szám_gyöke: int = int(math.sqrt(x)) + 1
    for osztó in range(3, szám_gyöke, 2):
        if x % osztó == 0:
            return False
    return True


def main() -> None:
    # Töltsünk fel egy listát 3db, 11-51 között páratlan számmal véletlenszerűen
    # Döntse el, hogy a listában található-e príszám!
    # A keresést ne folytassa, ha a választ meg tudja adni!
    számok: list[int] = []
    while len(számok) < 3:
        vszám: int = random.randint(11, 51)
        if vszám % 2 == 1:
            számok.append(vszám)
    van_prím = False
    print(számok)
    for szám in számok:
        if príme(szám):
            van_prím = True
            break
    print(f'A listában {"van" if van_prím else "nincs"} prímszám!')


if __name__ == "__main__":
    main()
