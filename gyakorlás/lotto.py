# kérj be két számot- melyik issebb melyik nagyobb
# megszerkesthetőe egy háromszög
# háromszög kerület/terület (héron képlet)
# téglalap kerület/terület


# kérjünk be a felhasználótól 5 db számot
# kritérium 1-90 ha nem teljesül kérjünk új számot
# kérjünk új számot ha ismétlődik
# határozzuk meg és írjuk ki a lottószámok átlagát

def lotto():
    print('Lotto')

    lottery_numbers: list[int] = []
    while len(lottery_numbers) != 5:
        inum: int = 0
        bad_number: bool = True
        while bad_number:
            inum: int = int(input(f'kérem az {len(lottery_numbers) + 1}. számot'))
            if inum < 1 or inum > 90:
                bad_number = True
                print('a lottoszám nincs 1 és 90 között')
            else:
                bad_number = False
        if inum not in lottery_numbers:
            lottery_numbers.append(inum)
        else:
            print('a lottószám már szerepel')

    osszeg: int = 0
    for num in lottery_numbers:
        osszeg += num

    print(f'a lottószámok átlaga:{osszeg / 5}')


lotto()
