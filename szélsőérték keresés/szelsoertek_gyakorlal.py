# keresztnevek.txt állományból olvassuk be és tároljuk a keresztneveket
# határozzuk meg és írjuk ki az 1. leghosszabb keresztnevet

def szelsoertek():
    keresztnevek: list[str] = []
    with open('keresztnevek.txt', 'r', encoding='utf-8') as file:
        for row in file.read().splitlines():
            keresztnevek.append(row)
    maxhossz: str = keresztnevek[0]
    for aktname in keresztnevek[1:]:
        if len(aktname) > len(maxhossz):
            maxhossz = aktname
    print(f'A leghosszabb keresztnév a listában: {maxhossz}')
    

szelsoertek()
