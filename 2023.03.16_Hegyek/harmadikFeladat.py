from Megoldas import *

m = Megoldas()
print("3.2 feladat: Az épületek száma: ", m.GetSzam())

print("3.3 feladat: Az épületek összes emeleteinek száma: ", m.SumEmeletek())

legmagasabb = m.LegmagasabbEpulet()
print(f"3.4 feladat: A legmagasabb épület adatai:\n\tNév: {legmagasabb.Nev}\n\tVáros: {legmagasabb.Varos}\n\tOrszág: {legmagasabb.Orszag}\n\tMagasság: {legmagasabb.Magassag} m\n\tEmeletek száma: {legmagasabb.Emelet}\n\tÉpítés éve: {legmagasabb.Epult}")

if m.OlaszKeres():
    print("3.5 feladat: Van olyan épület, amelyet Olaszország épített.")
else:
    print("3.5 feladat: Nincs olyan épület, amelyet Olaszország épített.")
