import random


def main() -> None:
    KERESZTNÉV_BANK: list[str] = ["Andrea", "Anna", "Bence", "Gizella", "Dénes", "Gyula", "Balázs",
                                  "Tamás", "Tibor", "Marcell", "Lili", "Erzsébet", "Mária", "Gábor",
                                  "Marietta", "Péter", "Zalán", "Zénó", "Adrienn", "Attila"]

    keresztnevek: list[str] = []
    while len(keresztnevek) < 10:
        vél_index = random.randint(0, len(KERESZTNÉV_BANK) - 1)
        if KERESZTNÉV_BANK[vél_index] not in keresztnevek:
            keresztnevek.append(KERESZTNÉV_BANK[vél_index])
    ikeresztnév: str = input('Kérem a keresztnevet: ')
    van_a_listában: bool = False
    for név in keresztnevek:
        if név == ikeresztnév:
            van_a_listában = True
            break
    print(f'A keresztnév {"" if van_a_listában else " nem"} szerepel a listában!')
    print(f'A keresztnév{"" if ikeresztnév in keresztnevek else " nem"} szerepel a listában!')

    print(f'Kiválasztott keresztnevek:\n{keresztnevek}')


if __name__ == "__main__":
    main()
