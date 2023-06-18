from time import time


def osztóharmonikus2():
    for n in range(1, 30000):
        if n % 2 != 0:
            continue
        osztók = [1 / n]
        for x in range(1, int(n / 2) + 1):
            if n % x == 0:
                osztók.append(1 / x)
        if round(len(osztók) / sum(osztók), 4).is_integer():
            print(n)


def main() -> None:
    startTime = time()
    osztóharmonikus2()
    endTime = time() - startTime
    print(f"it took {round(endTime, 4)}ms to run")


if __name__ == "__main__":
    main()
