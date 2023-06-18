from Megoldas import Megoldas


def main() -> None:
    # 2. feladat:
    m: Megoldas = Megoldas('egyszamjatek.txt')

    print(f'3. feladat: Játékosok száma: {m.jatekosok_szama}')

    print(f'4. feladat: Fordulók száma: {m.fordulok_szama}')

    print(f' 5. feladat: Az első sorban {"" if m.volt_egyes_tipp else "nem"} volt egyes tipp!')

    print(f'6. feladat: Legnagyobb tipp a fordulók során: {m.jatek_legnagyobb_tippje}')

    input_fordulo: int = int(input('7. feladat: Kérem a forduló sorszámát [1-{m.fordulok_szama}]:'))

    # HF: try-except, hogy "alma" inputnál 1 legyen az input_fordulo + 8.feladat
    if input_fordulo < 1 or input_fordulo > m.fordulok_szama:
        input_fordulo = 1


if __name__ == "__main__":
    main()
