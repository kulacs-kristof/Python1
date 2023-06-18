print("Kérek két természetes számot:")
tol = int(input("tól = "))
ig = int(input("ig = "))

tokeletesSzamokTartomanyban = []


def szamVizsgalas(szam):
    osztok = []
    tmpSzam = 2
    while tmpSzam < szam:
        if szam % tmpSzam == 0:
            osztok.append(tmpSzam)
        tmpSzam += 1

    return sum(osztok) + 1 == szam


# Szamok vizsgalasa
print(f"Tökéletes számok {tol} - {ig} között:")
for i in range(tol, int(ig / 2) + 1):
    if szamVizsgalas(i):
        tokeletesSzamokTartomanyban.append(i)

# Kiiras
if len(tokeletesSzamokTartomanyban) > 0:
    print(tokeletesSzamokTartomanyban[0], end="")
    for szam in tokeletesSzamokTartomanyban[1:]:
        print(f"; {szam}", end="")
else:
    print("A megadott tartományban nincsen tökéletes szám!")
