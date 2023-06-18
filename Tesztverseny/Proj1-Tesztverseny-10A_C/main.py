from Megoldasok import Megoldasok


def main() -> None:

    # 1.feladat:

    print('1. feladat: Az adatok beolvasása\n')
    m = Megoldasok('valaszok.txt')

    # 2.feladat:

    print(f'2. feladat: A vetélkedőn {m.versenyzok_szama} versenyző indult.\n')

    # 3.feladat:

    bekert_azonosito: str = str(input('3. Feladat: A versenyző azonosítója = '))
    print(f'{m.valaszok(bekert_azonosito)} (a versenyző válasza) \n')
    m.valaszok(bekert_azonosito)

    # 4.feladat:

    print('4. feladat:')
    print(m.helyes_megoldas, '(a helyes megoldás)')
    print(f' {m.megoldas}(a versenyző helyes válaszai)\n')

    # 5.feladat:

    try:
        keresett_id = int(input('5.feladat: A feladat sorszáma = '))
        megoldas = m.feladat_index(keresett_id)
        print(f'A feladatra {megoldas[0]} fő, a versenyzők {megoldas[1]}-a adott helyes választ. \n')
    except IndexError:
        print('Nincs ilyen számú kérdés\n')

    # 6.feladat:

    print("6. feladat: A versenyzők pontszámának meghatározása\n")
    eredmenyek = m.versenyzok_pont_szama
    m.fájl_kiírás(eredmenyek)

    # 7.feladat:

    print("7. feladat: A verseny legjobbjai:")
    print(m.legjobbak)


if __name__ == "__main__":
    main()
