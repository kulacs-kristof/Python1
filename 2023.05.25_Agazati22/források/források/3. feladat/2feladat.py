import random

for i in range(8):
    lista = []
    isHalmaz = True

    for x in range(5):
        ujszam = random.randint(0, 9)
        if ujszam in lista:
            isHalmaz = False

        lista.append(ujszam)
    
    print(i+1, " ", lista, end=" ")
    if isHalmaz:
        print("Halmaz")
        break
    else:
        print("Nem halmaz")

    