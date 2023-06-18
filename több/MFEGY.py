def main() -> None:

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    x = None
    x2 = None

    if a != 0:
        if b ** 2 >= 4 * a * c:
            if b ** 2 > 4 * a * c:
                print("Két gyök!")
                x = (-b + (b * b - 4 * a * c)**0.5) / (2 * a)
                x2 = (-b - (b * b - 4 * a * c)**0.5) / (2 * a)
                print(f"{x}, {x2}")
            else:
                print("Egy gyök!")
                x = -b / (2 * a)
                print(x)
        else:
            print("Nincs valós gyök!")
    else:
        print("Nem másodfokú!")
        if b != 0:
            x = -c / b
            print(x)
        else:
            if c != 0:
                print("Ellentmondás!")
            else:
                print("Azonosság!")


if __name__ == "__main__":
    main()
