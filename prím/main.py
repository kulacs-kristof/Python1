num = int(input("Adjon meg egy számot: "))

prím = False

if num > 1:
    for x in range(2, num):
        if (num % x) == 0:
            prím = True
            break
    if num == 0:
        prím = True

if prím:
    print(num, "nem prím szám")
else:
    print(num, "prím szám")
