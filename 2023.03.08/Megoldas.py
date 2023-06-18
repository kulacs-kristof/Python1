from Karakter import Karakter


class Megoldas(object):
    _karakterek: list[Karakter] = []

    def __init__(self, forras: str) -> None:
        with open(forras, 'r', encoding='utf-8') as file:
            sorok: list[str] = file.read().splitlines()
            betu: str = ''
            matrix: list[list[int]] = [[]]
            for sor in sorok:
                if len(sor) == 1:
                    betu = sor
                else:
                    for k in sor:
                        matrix[0][0] = int(k)
