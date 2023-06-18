from Karakter import Karakter


class Megoldas(object):
    karakter_bank: list[Karakter] = []

    def __init__(self, forras: str) -> None:
        with open(forras, 'r', encoding='UTF8') as file:
            sorok: list[str] = file.read().splitlines()
