from Eredmeny import Eredmeny


def main() -> None:
    # 1. Olvassa be az ub2017egyeni.txt állományban lévő adatokat és tárolja el
    # egy saját osztály típusú listában!
    # Ügyeljen arram, hogy az állomány első sora a mezőneveket tartalmazza.
    eredmények: list[Eredmeny] = []
    with open('ub2017egyeni.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            eredmények.append(Eredmeny(sor))

    # 2. Határozza meg és írja ki a minta szerint a képernyőre
    # a versenyen elindult futók számát!
    # Minta: 2. feladat: Futók száma: 186
    print(f'2. feladat: Futók száma: {len(eredmények)} fő')

    # 3. Számolja meg és írja ki a képernyőre a minta szerint,
    # hogy hány női sportoló teljesítette a teljes távot!
    nők100: int = 0
    for e in eredmények:
        if e.őNő and e.táv_teljesítve:
            nők100 += 1
    print(f'3. feladat: Távot teljesítő női versenyzők száma: {nők100} fő')

    # 4. feladat: Határozzuk meg a leghosszabb nevű futót/futókat és és írjuk ki az adatait a minta szerint!
    # Holtverseny esetén csak a futok neveit írjuk egymás mellé a minta szerint!
    # 4.1 Meghatározzuk a leghosszabb név hosszát:
    print('4. feladat: A leghosszabb nevű versenyző(k)')
    max_név_hossz: int = 0
    for e in eredmények:
        if e.név_hossza > max_név_hossz:
            max_név_hossz = e.név_hossza

    # 4.2 Kiválogajuk egy új listába a leghosszabb nevű futókat:
    max_névhoszz_eredmények: list[Eredmeny] = []
    for e in eredmények:
        if e.név_hossza == max_név_hossz:
            max_névhoszz_eredmények.append(e)
    # 4.3 Kiírás:
    if len(max_névhoszz_eredmények) > 1:
        for e in max_névhoszz_eredmények:
            print(f'\t{e.név}')
    else:
        print(f'\tNév: {max_névhoszz_eredmények[0].név}')
        print(f'\tRajtszám: {max_névhoszz_eredmények[0].rajtszám}')
        print(f'\tKategóra: {max_névhoszz_eredmények[0].kategória}')
        print(f'\tIdő: {max_névhoszz_eredmények[0].idő}')
        print(f'\tTáv százalék: {max_névhoszz_eredmények[0].táv_százalék}')

    # 5. Határozza meg és írja ki a minta szerint a teljes távot teljesítő
    # férfi sportolók átlagos idejét órában!
    # Feltételezheti, hogy legalább egy ilyen sportoló volt.
    szum_idő: float = 0
    férfi100_fő: int = 0
    for e in eredmények:
        if not e.őNő and e.táv_teljesítve:
            szum_idő += e.idő_órában
            férfi100_fő += 1
    print(f'5. feladat: Átlagos idő: {szum_idő / férfi100_fő}')

    # 6. feladat: Kategóránként határozza meg és írja ki a verseny győzteseit
    print('6. feladat: Verseny győztesei')
    győztes_ffi = None
    győztes_nő = None
    for e in eredmények:
        if e.táv_teljesítve:
            if e.őNő:
                if győztes_nő is None:  # Első nő, kinevezzük győztesnek
                    győztes_nő = e
                else:  # Ha már van győztes nő
                    if e.idő_órában < győztes_nő.idő_órában:
                        győztes_nő = e
            else:
                if győztes_ffi is None:  # Első férfi, kinevezzük győztesnek
                    győztes_ffi = e
                else:  # Ha már van győztes férfi
                    if e.idő_órában < győztes_ffi.idő_órában:
                        győztes_ffi = e

    if győztes_nő is not None:
        print(f'\tNők: {győztes_nő.név} ({győztes_nő.rajtszám}.) - {győztes_nő.idő}')
    if győztes_ffi is not None:
        print(f'\tFérfiak: {győztes_ffi.név} ({győztes_ffi.rajtszám}.) - {győztes_ffi.idő}')


if __name__ == "__main__":
    main()
