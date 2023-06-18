
print('1. feladat: Az adatok beolvasása')
forras = open('valaszok.txt', encoding='windows-1250')
lista = []
for i in forras:
    sor = i.strip().split(' ')
    lista.append(sor)
forras.close()

print()
print('2. feladat: A vetélkedőn', len(lista) - 1, 'versenyző indult.')
print()


def keres(azonosito, lista):
    for i in range(len(lista)):
        if lista[i][0] == azonosito:
            return lista[i][1]


adat = input('3. feladat: A versenyző azonosítója = ')

valasz = keres(adat, lista)
kulcs = str(lista[0][0])
print(keres(adat, lista), '(a versenyző válasza)')
print()

print('4. feladat:')
print(lista[0][0], '(a helyes megoldás)')

for j in range(len(kulcs)):
    if kulcs[j] == valasz[j]:
        print('+', end='')
    else:
        print(' ', end='')
print(' (a versenyző helyes válaszai)')
print()


def megoldas(sorszam, lista):
    szamol = 0
    for i in range(1, len(lista)):
        if lista[i][1][sorszam - 1] == lista[0][0][sorszam - 1]:
            szamol += 1
        else:
            szamol += 0
    return szamol


melyik = int(input('5. feladat: A feladat sorszáma = '))

print('A feladatra ', megoldas(melyik, lista), ' fő, a versenyzők ', round(megoldas(melyik, lista) / (len(lista) - 1) * 100, 2),
      '%-a adott helyes \nválaszt.', sep='')
print()


def pontszam(azonosito, lista):
    szamol = 0
    for i in range(1, len(lista)):
        if lista[i][0] == azonosito:
            for j in range(len(lista[i][1])):
                if j in [0, 1, 2, 3, 4] and lista[i][1][j] == lista[0][0][j]:
                    szamol += 3
                elif j in [5, 6, 7, 8, 9] and lista[i][1][j] == lista[0][0][j]:
                    szamol += 4
                elif j in [10, 11, 12] and lista[i][1][j] == lista[0][0][j]:
                    szamol += 5
                elif j in [13] and lista[i][1][j] == lista[0][0][j]:
                    szamol += 6
        else:
            szamol += 0
    return szamol


print('6. feladat: A versenyzők pontszámának meghatározása')
celfajl = open('pontok.txt', 'w', encoding='windows-1250')
for i in range(1, len(lista)):
    eredmeny = pontszam(lista[i][0], lista)
    print(lista[i][0], eredmeny, file=celfajl)
celfajl.close()
print()

print('7. feladat: A verseny legjobbjai:')
pontszamok = []
forrasfajl = open('pontok.txt', encoding='windows-1250')
for i in forrasfajl:
    sor = i.strip().split()
    sor[1] = int(sor[1])
    pontszamok.append(sor)
forrasfajl.close()

halmaz = set()
for x in range(len(pontszamok)):
    halmaz.add(pontszamok[x][1])
halmaz = sorted(list(halmaz), reverse=True)

for y in halmaz:
    for z in range(len(pontszamok)):
        if pontszamok[z][1] == y and halmaz.index(y) + 1 <= 3:
            print(halmaz.index(y) + 1, '. díj (', y, ' pont): ', pontszamok[z][0], sep='')
