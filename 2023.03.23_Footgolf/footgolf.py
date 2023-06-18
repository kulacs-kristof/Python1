from megoldas import *

m = Megoldas()

print(m.getVersenyzoSzama())

print(f"{m.getNoiVersenyzoSzazalek()}%")

bajnokNo = m.getNoiBajnok()

print("6.feladat: A női bajnok neve és az országa: ", bajnokNo.Nev, bajnokNo.osszPontszam())

stat = m.StatKeszit()
for key, value in stat.items():
    if value > 2:
        print(f"{key} - {value} fő")
