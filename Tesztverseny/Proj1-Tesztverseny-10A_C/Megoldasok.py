
from Valaszok import Valaszok


class Megoldasok:
    _valaszok_list: list[Valaszok]
    helyes_megoldas: str
    válaszok: str = ''

    @property
    def m_lista(self):
        return self._valaszok_list

    # 1.feladat:

    def __init__(self, fájl_neve: str):
        self._valaszok_list = []
        with open(fájl_neve, 'r', encoding='utf-8') as file:
            for index, sor in enumerate(file.read().splitlines()):
                if index == 0:
                    self.helyes_megoldas = sor
                else:
                    self._valaszok_list.append(Valaszok(sor))

    # 2.feladat:

    @property
    def versenyzok_szama(self) -> int:
        return len(self._valaszok_list)

    # 3.feladat:

    def valaszok(self, azonosito: str) -> str:
        for versenyzo in self._valaszok_list:
            if versenyzo.azonosito == azonosito:
                self.válaszok: str = str(versenyzo.valaszok)
                return self.válaszok
        return "Nincs ilyen azonosító."

    # 4.feladat:

    @property
    def megoldas(self):
        szöveg: str = ""
        for i, e in enumerate(self.válaszok):
            if e == self.helyes_megoldas[i]:
                szöveg += "+"
            else:
                szöveg += " "
        return szöveg

    # 5.feladat:

    def feladat_index(self, keresett_id: int):
        helyes_megoldasok_szama: int = 0
        for i in self._valaszok_list:
            if i.valaszok[keresett_id - 1] == self.helyes_megoldas[keresett_id - 1]:
                helyes_megoldasok_szama += 1
        return [helyes_megoldasok_szama, round((helyes_megoldasok_szama / len(self._valaszok_list) * 100), 2)]

    verseny_stat: dict[str, int] = {}

    # 6.feladat:

    @property
    def versenyzok_pont_szama(self):
        for e in self._valaszok_list:
            i: int = 0
            pontok: int = 0
            while len(self.helyes_megoldas) != i:
                if e.valaszok[i] == self.helyes_megoldas[i]:
                    if i <= 4:
                        pontok += 3
                    elif 9 >= i > 4:
                        pontok += 4
                    elif 12 >= i > 9:
                        pontok += 5
                    elif i > 12:
                        pontok += 6
                i += 1

            if e.azonosito not in self.verseny_stat:
                self.verseny_stat[e.azonosito] = pontok
        return self.verseny_stat

    def fájl_kiírás(self, kiirando_allomany: dict[str, int]):
        with open('pontok.txt', 'w', encoding='utf-8') as file:
            for kulcs, ertek in kiirando_allomany.items():
                file.write(f'{kulcs} {ertek}\n')
        file.close()

    # 7.feladat:

    @property
    def legjobbak(self):
        tempdict: dict[str, int] = dict(sorted(self.verseny_stat.items(), key=lambda item: item[1]))

        utolsó_pont: int = 0
        helyezett: int = 1

        szoveg: str = ""

        for index in range(0, 5):
            azonosito: str = list(tempdict.keys())[len(tempdict) - index - 1]
            eredmeny: int = list(tempdict.values())[len(tempdict) - index - 1]

            if utolsó_pont == eredmeny:
                helyezett -= 1

            if helyezett > 3:
                break

            szoveg += f"{helyezett}.díj ({eredmeny} pont): {azonosito}\n"

            utolsó_pont = eredmeny
            helyezett += 1

        return szoveg
