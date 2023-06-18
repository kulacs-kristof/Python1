import random
from time import sleep


def main() -> None:
    lottoszamok = []
    maxszam = 5
    while len(lottoszamok) < maxszam:
        szam = random.randint(1, 90)
        if szam not in lottoszamok:
            lottoszamok.append(szam)
    for szam in lottoszamok:
        sleep(0.5)
        print(szam, end=" ")
    print()


if __name__ == "__main__":
    main()
