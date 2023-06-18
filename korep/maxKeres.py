import random

def maxKeres():
    max = szamok[0]
    for szam in szamok:
        if szam > max:
            max = szam
    print(max)

szamok = []
for i in range(1,10+1):
    szamok.append(random.randint(1,1000))
print(szamok)
maxKeres()
print(max(szamok))
