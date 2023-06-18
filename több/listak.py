import time


def main() -> None:
    # Kollekciók: olyan adatszerkezetek, amelyek több adatot tárolnak
    # Fontosabb fajtái: listák, tuple-ök, szótárak
    # Mi a listákat típusos listáknak definiáljuk ami azt jelenti hogy a listaelemek típusa megegyezik
    # Alternatív nevek: tömbök, vektorok
    lista1: list[str] = []  # üres lista
    lista2: list[int] = list()  # lista konstruktorral is létrehozható
    lista3: list[str] = ["alma", "körte", "szilva"]
    lista4: list[int] = list(range(10))  # 0-tól 9-ig tartó lista

    # Hivatkozás a lista elemeire
    print(lista3[0])  # alma
    print(lista3[1])  # körte

    # Lista elemeikek módosítása
    lista3[0] = "barack"

    # Lista hossza
    print(len(lista3))  # 3

    # Lista elemeninek kiíratása
    print(lista3)  # ['barack', 'körte', 'szilva']
    # for loopal:
    for elem in lista3:
        print(elem)
    print()

    # speciális lista indexelés
    print(lista3[-1])  # szilva
    print(lista3[:1])  # ['barack']
    print(lista3[:2])  # ['barack', 'körte']
    print(lista3[1:3])  # ['körte', 'szilva']

    # szükségünk van az indexre
    for i, elem in enumerate(lista3):
        print(i, elem)

    # a lista indexét állítjuk előbb 0..len(lista)-1
    for i in range(len(lista3)):
        print(i, lista3[i])

    # Lista bővítése
    lista3.append("narancs")
    print(lista3)  # ['barack', 'körte', 'szilva', 'narancs']

    # Beszúrás a listába
    lista3.insert(1, "eper")
    print(lista3)  # ['barack', 'eper', 'körte', 'szilva', 'narancs']

    lista2.append(99)
    lista2.append(23)
    lista2.append(34)
    lista2.append(45)
    lista2.append(99)
    lista2.append(45)

    # HF:  remove, pop, clear, teljes lista törlése


if __name__ == "__main__":
    main()
