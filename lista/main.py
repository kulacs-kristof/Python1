import random


def main() -> None:
    print('megszámlálás programozási tétel')
    numbers: list[int] = []
    amount: int = random.randint(10, 15)
    for _ in range(amount):
        numbers.append(random.randint(10, 99))
    print(numbers)
    paros_db: int = 0
    for num in numbers:
        if num % 2 == 0:
            paros_db += 1
    print(f'A lista elemei: {numbers}')
    print(f'páros számok darabszáma a listában: {paros_db}')


# hf: páros indexű páros számok darabszáma


if __name__ == "__main__":
    main()
