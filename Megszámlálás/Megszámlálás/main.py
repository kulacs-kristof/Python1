import random


def main() -> None:
    print('Megszámlálás programozási tétel (típusfeladat)')
    # Töltsünk fel egy listát véletlenszerűen kétjegyű számokkal, a lista elemszáma
    # véletlenszerűen 10-15 tartományban legyen!
    # Állapítsuk meg a páros számok darabszámát!
    számok: list[int] = []
    elemszám: int = random.randint(10, 15)
    for _ in range(elemszám):
        számok.append(random.randint(10, 99))
    páros_számok_db: int = 0
    for szám in számok:
        if szám % 2 == 0:
            páros_számok_db += 1
    print(f'A lista elemei: {számok}')
    print(f'Páros számok darabszáma a listában: {páros_számok_db}')

    # HF: Páros indexű, páros számok darabszáma
    # Megoldás 1:
    páros_indexű_páros_számok_db: int = 0
    for (i, szám) in enumerate(számok):
        if i % 2 == 0 and szám % 2 == 0:
            páros_indexű_páros_számok_db += 1
    print(f'Páros indexű páros számok darabszáma a listában: {páros_indexű_páros_számok_db}')

    # Megoldás 2:
    páros_indexű_páros_számok_db_2: int = 0
    for i in range(0, len(számok), 2):
        if számok[i] % 2 == 0:
            páros_indexű_páros_számok_db_2 += 1
    print(f'Páros indexű páros számok darabszáma a listában: {páros_indexű_páros_számok_db_2}')

    # Megoldás 3:
    páros_indexű_páros_számok_db_3: int = 0
    for szám in számok[::2]:
        if szám % 2 == 0:
            páros_indexű_páros_számok_db_3 += 1
    print(f'Páros indexű páros számok darabszáma a listában: {páros_indexű_páros_számok_db_3}')

    # Lista mint halmaz kezelése
    # Halmazban lévő páratlan számok darabszáma
    # Határozuk meg az "ütközések" átlagos számát 100000-es minta alapján
    ütközések_száma_összeg: int = 0
    for _ in range(10000):
        halmaz: list[int] = []
        elemszám: int = 80
        ütközések_száma: int = 0
        while len(halmaz) < elemszám:
            szám: int = random.randint(10, 99)
            if szám not in halmaz:
                halmaz.append(szám)
            else:
                ütközések_száma += 1
        # print(halmaz)
        # print('Nincs a halmazban : ')
        # for vszám in range(10, 100):
        #     if vszám not in halmaz:
        #         print(f'{vszám}, ', end='')
        # print(f'Ütközések száma: {ütközések_száma}')
        ütközések_száma_összeg += ütközések_száma
    print(f'Ütközésszám átlag 10000-es próba alapján: {ütközések_száma_összeg / 10000}')


if __name__ == "__main__":
    main()
