import random


def szelsoeretek():
    print('Szélsőérték keresése')
    numbers: list[int] = []
    for _ in range(10):
        numbers.append(random.randint(10, 99))
    print(numbers)
    maximum: int = numbers[0]
    for akt_elem in numbers[1:]:
        if akt_elem > maximum:
            maximum = akt_elem
    print(f'A lista legnagyobb értékű eleme: {maximum}')
    minimum: int = numbers[0]
    for akt_elem in numbers[1:]:
        if akt_elem < minimum:
            minimum = akt_elem
    print(f'A lista legkisebb értékű eleme: {minimum}')
    maxi: int = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[maxi]:
            maxi = i
    print(f'A lista legnagyobb értékű eleme: {numbers[maxi]}')
    print(f'Indexe: {maxi}')
    numbers[2] = 99
    numbers[8] = 99
    print(numbers)
    maxilast: int = 0
    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[maxilast]:
            maxilast = i
    print(f'A lista legnagyobb értékű eleme: {numbers[maxilast]}')
    print(f'Indexe: {maxilast}')
    maxiparatlan: int = -1  # -1 marad ha nincs páratlan a listában
    for i, e in enumerate(numbers):  # i index, e érték
        if e % 2 == 1:
            if maxiparatlan == -1:  # az 1. páratlan szám a listában
                maxiparatlan = i
            else:  # nem az 1, páratlan
                if e > numbers[maxiparatlan]:
                    maxiparatlan = i
    if maxiparatlan == -1:
        print('nincs páratlan a listában')
    else:
        print(f'A legnagyobb páratlan szám: {numbers[maxiparatlan]}')
        print(f'Indexe: {maxiparatlan}')
    maxparatlan: int = -1
    for aktnum in numbers:
        if aktnum % 2 == 1 and aktnum > maxparatlan:
            maxparatlan = aktnum
        if maxparatlan == -1:
            print('nincs páratlan')
        else:
            print(f'legnagyobb páratlan szám: {maxparatlan}')


szelsoeretek()
