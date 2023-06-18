def main() -> None:
    x: int = int(input("Adj meg egy számot\n"))   
    if x < 0:
        x = -x
    print("Abs(x) = ", x)
    
    x: int = int(input("Adj meg egy számot\n"))   
    print(f"A(z) {x} abszolút értéke ", end="")
    if x < 0:
        x = -x
    print(x)


if __name__ == "__main__":
    main()
