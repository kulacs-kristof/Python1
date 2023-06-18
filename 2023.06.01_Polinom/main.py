from datetime import datetime

szamok = " "
polinomok = []

f = open("eh.txt", "w", encoding="utf-8")

def isInt(szoveg):
    return szoveg.replace(" ", "").isnumeric()

def isDuplicate(polinom):
    return polinom in polinomok

def Osszerakas(lista, nullaFilter):
    kesz_muvelet = []
    muveletek = ["x^3", "x^2", "x", ""]

    for i in range(len(muveletek)):
        if lista[i] == 0 and nullaFilter:
            continue
            
        kesz_muvelet.append(str(lista[i])+muveletek[i])
    
    return "+".join(kesz_muvelet)

def Korrigal(lista):
    if len(lista) > 4:
        print("Több együttható lett megadva! A felesleg le lesz vágva!")
        while len(lista) > 4:
            lista.pop()

    if len(lista) < 4:
        while len(lista) < 4:
            lista.append(0)
    
    return lista

while szamok != "":
    szamok = input("Adjon meg max 4 számot szóközzel elválasztva: ").strip()

    if not isInt(szamok):
        continue

    szamok = szamok.split(" ")

    szamok = Korrigal(szamok)
    szamok.reverse()

    #NULLA FILTER
    polinom = Osszerakas(szamok, False)

    #SZŰRÉS
    if not isDuplicate(polinom):
        f.write(f"{polinom}\n")
        polinomok.append(polinom)

f.write(str(datetime.now().isocalendar().week))
f.close()