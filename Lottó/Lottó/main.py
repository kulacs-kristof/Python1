import random


def main() -> None:
    print('LOTTO')
    print('Ha ezeket a számokat szombaton megjátszod az ötös lottón, akkor milliárdos is lehetsz!')
    sorsolt_számok: list[int] = []
    while len(sorsolt_számok) < 5:
        vél_szám: int = random.randint(1, 90)
        if vél_szám not in sorsolt_számok:
            sorsolt_számok.append(vél_szám)
    print(f'Szombaton ezekkel a számokkal nyerhetsz: {sorsolt_számok}')


if __name__ == "__main__":
    main()
