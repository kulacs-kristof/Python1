

def beolvas(allomany_neve: str) -> list[str]:
    sorok: list[str] = []
    try:
        with open(allomany_neve, 'r', encoding='utf-8') as file:
            sorok = file.read().splitlines()
    except Exception as ex:
        print(f'hiba: {ex}')
    return sorok


def osszeg(sor: str) -> int:
    return len(sor)


def num():
    sorok: list[str] = beolvas('szamok.txt')
    if len(sorok) > 0:
        for sor in sorok:
            print(f'{sor} -> {osszeg(sor)}')
    else:
        print('Probléma az állomány beolvasásakor!')


num()
