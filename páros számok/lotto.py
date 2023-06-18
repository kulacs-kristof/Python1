import random

hány_számból = 90
hány_számot = 5

random.seed()
halmaz = set()
while len(halmaz) < hány_számot:
    halmaz.add(random.randint(1, hány_számból))
számlista = sorted(list(halmaz))

print("A heti lottószámok: ", ", ".join(str(szám) for szám in számlista))
