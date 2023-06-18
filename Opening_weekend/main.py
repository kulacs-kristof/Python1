from Film import Film


def main() -> None:
    # 3.1 Olvassa be az UTF-8 kódolású  nyitohetvege.txt állományban lévő adatokat
    # és tárolja el egy saját osztály típusú listában!
    # Ügyeljen rá, hogy az állomány első sora az adatok fejlécét tartalmazza!
    filmek: list[Film] = []
    with open('nyitohetvege.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            filmek.append(Film(sor))

    # 3.2 Határozza meg és írja ki a képernyőre a minta szerint,
    # hogy hány filmbemutató található az állományban!
    print(f'3.2 feladat: Filmek száma az állományban: {len(filmek)} db')

    # 3.3  Összesítse és írja ki a képernyőre a UIP Duna Film forgalmazó
    # (forgalmazó="UIP") első hetes bevételeinek összegét!
    # Az összeg ezres szeparátorral jelenjen meg a minta szerint!
    össz_bevétel: int = 0
    for f in filmek:
        if f.ez_UIP:
            össz_bevétel += f.bevetel
    össz_bevétel_str: str = f'{össz_bevétel:,} Ft'.replace(',', ' ')
    print(f'3.3 feladat: UIP Duna Film forgalmazpó 1. hetes bevételeinek összege: {össz_bevétel_str}')

    # 3.4  Határozzuk meg az átlagos nézőszámot az InterCom által forgalmazott
    # filmek esetében! Feltételezheti, hogy legalább 1 filmet forgalmazott a cég.
    # Az átlagot a minta szerint 1 tizedesjegyre kerekítve jelenítse meg!
    intercom_össz_néző: int = 0
    intercom_össz_film_db: int = 0
    for f in filmek:
        if f.ez_intercom:
            intercom_össz_néző += f.latogato
            intercom_össz_film_db += 1
    print(f'3.4 feladat: InterCom átlagos nézőszám: {intercom_össz_néző / intercom_össz_film_db:.2f}')
    átlag_kerekítve: float = round(intercom_össz_néző / intercom_össz_film_db, 2)
    print(f'3.4 feladat: InterCom átlagos nézőszám: {átlag_kerekítve}')

    # 3.5 Kérjen be egy évszámot majd döntse el, hogy az adatok között
    # található-e a megadott évben bemutatott film!
    # A keresését ne folytassa, ha a választ meg tudja adni!
    # A képernyőre írást a minta szerint végezze!
    vizsgált_évszám: int = int(input('3.5 feladat: Kérem a vizsgált évszámot: '))
    volt_bemutató: bool = False
    for f in filmek:
        if f.bemutató_éve == vizsgált_évszám:
            volt_bemutató = True
            break
    # if volt_bemutató:
    #     print('3.5 A megadott évben volt bemutató.')
    # else:
    #     print('3.5 a megadott évben nem volt nemutató.')
    print(f'\tA megadott évben {"nem " if volt_bemutató else ""} volt bemutató')


if __name__ == "__main__":
    main()
