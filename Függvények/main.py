import random


def összead(a: int, b: int, c: int) -> int:
    return a + b + c


def main() -> None:
    összead(3, 4, 5)
    print(összead(3, 4, 5))
    összeg: int = összead(5, 6, 7)
    print(összeg)

    x1: int = random.randint(-5, 5)
    x2: int = random.randint(-5, 5)
    x3: int = random.randint(-5, 5)

    if összead(x1, x2, x3) < 0:
        print('Az összeg nullánál kisebb')
    else:
        print('Az összeg nulla vagy pozitív')


if __name__ == "__main__":
    main()
