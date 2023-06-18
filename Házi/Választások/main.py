from Megoldas import Megoldas


def main() -> None:
    # 1. feladat: Beolvasás
    mo: Megoldas = Megoldas('szavazatok.txt')

    print(f'2. feladat: A helyhatósági választásokon {mo.kepviselok_szama} képviselőjelölt indult.')

    kepviselo_neve: str = input('3. feladat: Kérem a képvisellő nevét: ')
    print(mo.kepviselo_keresese(kepviselo_neve))

    print(f'4. feladat: A választáson {mo.resztvevok_szama} állampolgar, a jogosultak {mo.resztvevok_szazaleka:.2f}%-a vett részt.')

    print('5. feladat: Statisztika')
    print(mo.szavazatok_stat)

    print('6. felaadat: Győztes képviselő(k)')
    print(mo.gyoztes_kepviselok)


if __name__ == "__main__":
    main()
