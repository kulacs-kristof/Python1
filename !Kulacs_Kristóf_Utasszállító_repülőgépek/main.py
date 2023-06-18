from Repcsi import Repcsi


def main() -> None:
    # 3. feladat
    repcsik: list[Repcsi] = []
    with open('utasszallitok.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            repcsik.append(Repcsi(sor))

    print(f'4. feladat: Adatsorok száma: {len(repcsik)}')

    # 5. feladat:
    boeing_db: int = 0
    for r in repcsik:
        if r.típus.startswith('Boeing'):
            boeing_db += 1
    print(f'5. feladat: Boeing típusok száma: {boeing_db}')

    # 6. feladat:
    max_utas_repülő: Repcsi = repcsik[0]
    for r in repcsik[1:]:
        if r.max_utas > max_utas_repülő.max_utas:
            max_utas_repülő = r
    print('6. feladat: A legtöbb utast szállító repülőgéptípus')
    print(max_utas_repülő.adatok)

    print('7. feladat:')
    stat: dict[str, int] = {
        'Alacsony sebességű': 0,
        'Szubszonikus': 0,
        'Transzszonikus': 0,
        'Szuperszonikus': 0
    }

    for r in repcsik:
        stat[r.sebesség_kategória] += 1

    nullás_kategória: list[str] = []
    for k, v in stat.items():
        if v == 0:
            nullás_kategória.append(k)

    if len(nullás_kategória) == 0:
        print('\tMinden sebességkategóriából van repülőgéptípus.')
    else:
        print('\t', end='')
        for kat in nullás_kategória:
            print(f'{kat} ', end='')
        print()  # soremelés

    # 8. feladat:
    # Készítsen utasszallitok_new.txt néven szöveges állományt a feladat végén található
    # minta szerint, melynek szerkezete, fejlécsora és adattartalma megegyezik az
    # utasszallitok.txt állományéval, a következő különbségekkel:
    # a. Az utasok számánál „tól-ig” érték esetén csak az „ig” érték kerüljön az új állományba.
    # b. A személyzet számánál is a „tól-ig” érték esetén csak az „ig” érték kerüljön az állományba.
    # c. A felszállótömeg tonnában kifejezve, tetszőleges módszerrel egész értékre kerekítvekerüljön az adatsorokba. (1 kg = 0,001 t).
    # d. A fesztávolság láb mértékegységgel kifejezve, tetszőleges módszerrel egész értékre kerekítve kerüljön az adatsorokba. (1 m = 3,2808 láb)

    # 9. feladat
    # Határozza meg az adatforrásban lévő, 100 utasnál több szállítására alkalmas repülőgépek átlagos fesztávolságát!
    # Az eredményt tetszőleges formában írja a képernyőre!

    repulok: list[float] = []

    for r in repcsik:
        if r.max_utas > 100:
            repulok.append(r._fesztáv)

    atlagos_fesztav = sum(repulok) / len(repulok)

    print(f'9. feladat: A 100 utasnál többet szállító repülők atlagos fesztávolsága: {atlagos_fesztav} m')

    # 10. feladat:
    # Dönse el, hogy az az adatforrásban megtalálható-e olyan repülőgépp, amely 1989-ben tette meg az első útját!
    # Az eredményt tetszőleges formában írja a képernyőre!

    elso_ut = False

    for r in repcsik:
        if r._év == 1989:
            elso_ut = True
            break

    if elso_ut == True:
        print('10. feladat: Az adatforrásban található olyan repülőgép amely 1989-ben tette meg az első útját.')
    else:
        print('10. feladat: Az adatforrásban nincs olyan repülő amely 1989-ben tette meg az első útját.')

    # 11. feladat:
    # Határozza meg a legtöbb személyzetet szállító repülőgép adatait!
    # Az eredményt a 6. feladat mintája szerint írja a képernyőre!

    legtobb_szemely_repcsi: Repcsi = repcsik[0]
    for r in repcsik:
        if r._személyzet > legtobb_szemely_repcsi._személyzet:
            legtobb_szemely_repcsi = r

    print('11.feladat: A legtöbb személyzetet szállító repülőgéptípus')
    print(legtobb_szemely_repcsi.adatok, end='')


if __name__ == "__main__":
    main()
