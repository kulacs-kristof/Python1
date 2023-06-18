from Kolcsonzes import Kolcsonzes


def main() -> None:
    # 3. feladat:
    eredmenyek: list[Kolcsonzes] = []
    with open('badacsonybike.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            eredmenyek.append(Kolcsonzes(sor))

    print(f'3. feladat: Napi kölcsönzések száma: {len(eredmenyek)} ')

    # 4. feladat:
    rendszam: list[str] = []
    for e in eredmenyek:
        if e.azon not in rendszam:
            rendszam.append(e.azon)

    print(f'4. feladat: Kerékpárok száma: {len(rendszam)}')

    # 5. feladat:
    # ulolso: Kolcsonzes = eredmenyek[0]
    # for e in eredmenyek:
    #   if e.vissza_percekben_kifejezve > utolso.vissza_percekben_kifejezve:
    #      utolso = e
    print('5. feladat: A legkésöbb visszahozott kerékpár')
    print('Bérlő neve:')
    print('Kerékpár azonosítója:')
    print('Kölcsönzés ideje:')


if __name__ == "__main__":
    main()
