import random


def main() -> None:
    # Hozzunk létre egy konstans listát 20 keresztnévvel
    # Válasszunk ki véletlenszerűen 10 keresztnevet a listából ismétlődések elkerülésével
    # Kérjünk be egy keresztnevet a felhasználótól
    # Ellenőrizzük hogy a megadott keresztnév megtalálható-e a listában

    nevek = [
        "Ádám", "Béla", "Cecília", "Dániel", "Erika", "Ferenc", "Gábor", "Hanna",
        "István", "János", "Katalin", "László", "Mária", "Nóra", "Ottó", "Péter",
        "Róbert", "Sándor", "Tamás", "Zsuzsanna", "Kristóf", "Marcell", "Olivér",
        "Martin", "Háti", "Brigi", "Matyi", "Dominik", "Koppány", "Balázs", "Bálint",
        "Katrin", "Krisztián", "Norbert", "Hunor", "Zsigmond", "Ajsa", "Julianna",
        "Gábor", "László", "Lorin"
    ]

    valasztott_nevek = []

    while len(valasztott_nevek) != 10:
        valasztott_nev = nevek[random.randint(0, len(nevek) - 1)]
        if valasztott_nev not in valasztott_nevek:
            valasztott_nevek.append(valasztott_nev)

    user_nev = input("Kérem a keresztnevet: ")

    for nev in valasztott_nevek:
        if nev == user_nev.capitalize():
            print("A név megtalálható")
            break
    else:
        print("A név nem megtalálható")


if __name__ == "__main__":
    main()
