import marci


def main() -> None:
    print(marci.RED + 'Két szám legnagyobb közös osztója')
    a = int(input('Add meg az első számot: '))
    b = int(input('Add meg a második számot: '))
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(f'{a} és {b} legnagyobb közös osztója: {a}')


if __name__ == "__main__":
    main()
