import random


def main() -> None:
    jegyek = []
    atlag = 0
    for _ in range(13):
        jegyek.append(random.randint(1, 5))

    for szam in jegyek:
        if szam == 1:
            atlag = 1
            break
        else:
            atlag = round(sum(jegyek) / len(jegyek), 2)

    print(f"Jegyek: {jegyek}")
    print(f"Tanulmányi Átlag: {atlag}")
    print(f"Normál Átlag: {round(sum(jegyek) / len(jegyek), 2)}")
    print(f"Kiterjedés: {max(jegyek)-min(jegyek)}")
    print(f"Módusz: {max(set(jegyek), key=jegyek.count)}")
    print(f"Szórás: {round((sum([(x-sum(jegyek)/len(jegyek))**2 for x in jegyek])/len(jegyek))**0.5, 2)}")

    print("--------------------------")
    # Módosítsuk az átlagszámítást tanulmányi átlagra melynek a szabályai a következők:
    # Ha a tanulónak van 1ese akkor átlaga 1 egyes
    # Ha nincs akkkor átlaga hazározza meg a jegyek átlagát


if __name__ == "__main__":
    main()
