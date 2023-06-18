# Be kell kérni két számot és döntse el melyik a kisebb és nagyobb
# Be kell kérni 3 számot és el kell dönteni hogy a háromszög megszerkeszthető-e
# Háromszög kerület/terület számítás (héron képlet)
# Ellenőrizzük az inputot

def main() -> None:
    # Kérjünk be 5 számot (1-90), ha nem teljesül akkor kérjük be újra
    # Kérjük újra, ha már korábbi inputként szerepel
    # Határozzuk meg s írjuk ki a lottószámok átlagát
    szamok = []
    while len(szamok) < 5:
        try:
            inp: int = int(input(f"Kérem a {len(szamok)+1}. számot: "))
        except BaseException:
            print("Csak számot lehet beírni!")
            continue
        if isValid(inp):
            print(f"A szám {inp} nem esik a megfelelő tartományba")
            continue
        if inp in szamok:
            print(f"A szám {inp} már szerepel a tárolt számok")
            continue
        szamok.append(inp)
        print(f"Szám hozzáadva: {inp}")
        print(szamok)

    print(f"Beírt számok átlaga: {sum(szamok)/len(szamok)}")

    # Készíts egy függvényt ami igazzal tér vissza ha a megadott szám az 5ös lottó megfelelő értékű száma


def isValid(szam) -> bool:
    return szam < 1 or szam > 99


if __name__ == "__main__":
    main()
