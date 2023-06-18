def num(x: int) -> int:
    osztok: int = 0
    for oszto in range(1, x):
        if x % oszto == 0:
            osztok += oszto
    return osztok


def main() -> None:
    x: int = int(input('Kérek egy számot: '))
    if num(x) == x:
        print('Ez tökéletes szám')
    else:
        print('Ez nem tökéletes szám')


if __name__ == "__main__":
    main()
