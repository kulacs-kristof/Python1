def GetSzokoevek():
    nagyobb = 0
    kisebb = 0
    evek = []
    if ev1 > ev2:
        nagyobb = ev1
        kisebb = ev2
    else:
        nagyobb = ev2
        kisebb = ev1
    for evszam in range(kisebb, nagyobb+1):
        if(CheckEv(evszam)):
            evek.append(evszam)
    return evek

def CheckEv(ev):
    if ev % 400 == 0 or (ev % 4 == 0 and ev % 100 > 0):
        return True
    return False

print("2.Feladat: Szőkőév listázó")
ev1 = int(input("Kérem az egyik évszámot: "))
ev2 = int(input("Kérem a második évszámot: "))
szokoevek = GetSzokoevek()
if len(szokoevek) == 0:
    print("Nem volt szökőév a két megadott évszám között!")
else:
    print(szokoevek)
