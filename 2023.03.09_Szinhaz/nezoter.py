from megoldas import megoldas

m = megoldas()

'''
sor = input(f"Sor száma [1-{len(m.foglaltsagok)}]: ")
szek = input(f"Szék száma [1-{len(m.foglaltsagok[0])}]: ")

if m.getFoglaltsag(sor, szek):
    print(f"\tA {sor}. sor {szek}. szék foglalt!")
else:
    print(f"\tA {sor}. sor {szek}. szék szabad!")
'''

eredmeny = m.getArany()
print(f"3. feladat: Az előadásra eddig {eredmeny[0]} jegyet adtak el, ez a nézőtér {eredmeny[1]}%-a.")

print(f"4. feladat: A legtöbb jegyet a(z) {m.getKatLegtobb()} kategóriába értékesítették.")

print(f"5. feladat: A bevétel összege {m.bevetelSzamol()} Ft.")

print(f"6. feladat: Üres helyek száma: {m.getUresHelyek()}")
