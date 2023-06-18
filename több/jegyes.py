
def main() -> None:
    print("Érdemjegy")
    jegy = int(input("Kérem az osztályzatot [1-5]\n"))
    if jegy == 1:
        print("Elégtelen")
    elif jegy == 2:
        print("Elégséges")
    elif jegy == 3:
        print("Közepes")
    elif jegy == 4:
        print("Jó")
    elif jegy == 5:
        print("Jeles")
    else:
        print("Helytelen jegy!")


if __name__ == "__main__":
    main()
