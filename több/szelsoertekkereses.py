import random
import time


def main() -> None:
    # Szélsoérték keresés
    # Töltsünk fel egy listát 10 véletlen számmal
    # Határozzuk meg a legnagyobb számot a listában

    számok = []
    for _ in range(10):
        számok.append(random.randint(10, 99))

    print(számok)
    '''
    # Szélsoérték keresés
    legnagyobb = számok[0]
    for szám in számok:
        if szám > legnagyobb:
            legnagyobb = szám
    print(legnagyobb)

    # minimum
    legkisebb = számok[0]
    for szám in számok:
        if szám < legkisebb:
            legkisebb = szám
    print(legkisebb)

    # legnagyobb elem indexe és értéke
    index = 0
    for (i, elem) in enumerate(számok):
        if számok[i] > számok[index]:
            index = i
    print(f"Legnagyobb elem indexe: {index}, értéke: {számok[index]}")

    # Gatározzuk meg a legnagyobb elem indexét és értékét
    # Ha a legnagyobb elem többször is előfordul, akkor az utolsó elem indexe legyen meghatározva

    index = 0
    for (i, elem) in enumerate(számok):
        if számok[i] >= számok[index]:
            index = i
    print(f"Legnagyobb elem indexe: {index}, értéke: {számok[index]}")
    '''
    # Határozzuk meg a legnagyobb páratlan elem indexét és értékét
    index = -1
    for i, e in enumerate(számok):
        if e % 2 == 1 and (index == -1 or számok[i] > számok[index]):
            index = i
    print(f"Legnagyobb páratlan elem indexe: {index}, értéke: {számok[index]}" if index != -1 else "Nincs páratlan elem")

    # Határozzuk meg a legnagyobb párosatlan szám indexét
    páratlanszám = None
    for szám in számok:
        if szám % 2 == 1 and (páratlanszám == -1 or szám > páratlanszám):
            páratlanszám = szám
    if páratlanszám is not None:
        print(f"Legnagyobb páratlan szám: {páratlanszám}")
    else:
        print("Nincs páratlan szám")


if __name__ == "__main__":
    main()
