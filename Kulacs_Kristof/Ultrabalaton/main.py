from erredmeny import Eredmeny


def main() -> None:
    # 1. Olvassa be az ub2017egyeni.txt állományban lévő adatokat és tárolja el
    # egy saját osztály típusú listában!
    # Ügyeljen arram, hogy az állomány első sora a mezőneveket tartalmazza.
    eredmenyek: list[Eredmeny] = []
    with open('ub2017egyeni.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            eredmenyek.append(Eredmeny(sor))

    # 2. Határozza meg és írja ki a minta szerint a képernyőre
    # a versenyen elindult futók számát!
    # Minta: 2. feladat: Futók száma: 186
    print(f'2. feladat: futók száma: {len(eredmenyek)}')

    # 3. Számolja meg és írja ki a képernyőre a minta szerint,
    # hogy hány női sportoló teljesítette a teljes távot!
    nok100: int = 0
    for e in eredmenyek:
        if e.ono and e.tav_teljesitve:
            nok100 += 1
    print(f'3. feladat: Távot teljesítő női versenyzők száma: {nok100} fő')

    # 4. feladat: Határozzuk meg a leghosszabb nevű futót/futókat és és írjuk ki az adatait a minta szerint!
    # Holtverseny esetén csak a futok neveit írjuk egymás mellé a minta szerint!

    # 4.1 Meghatározzuk a leghosszabb név hosszát:

    # 4.2 Kiválogajuk egy új listába a leghosszabb nevű futókat:

    # 5. Határozza meg és írja ki a minta szerint a teljes távot teljesítő
    # férfi sportolók átlagos idejét órában!
    # Feltételezheti, hogy legalább egy ilyen sportoló volt.


if __name__ == "__main__":
    main()
