
def Vizsgal():
    db = 1
    print(f"{db}. szám: {1}")
    for num in range(1, 10000 + 1):
        osztok = []
        if num % 2 == 0:
            szamFele = int(num/2)
            for oszto in range(1, szamFele+1):
                if num % oszto == 0:
                    osztok.append(1 / oszto)
            osztok.append(1 / num)
            eredmeny = round(len(osztok) / sum(osztok), 4)
            if (eredmeny) % 1 == 0:
                db += 1
                print(f"{db}. szám: {num}")

Vizsgal()