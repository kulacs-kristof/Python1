# a keresztnevek txt állományból olvassuk be és tűroljuk el a keresztneveket
# Határozzuk meg és írjuk ki az első leghosszabb keresztnevet

def main() -> None:
    keresztnevek = []
    leghosszabb = ""
    legrövidebb = ""
    betűk = {"a": 1}
    with open("Keresztnevek.txt", "r", encoding="utf-8") as file:
        for sor in file.read().splitlines():
            keresztnevek.append(sor)

    legrövidebb = keresztnevek[0]
    leghosszabb = legrövidebb
    for név in keresztnevek:
        if len(leghosszabb) < len(név):
            leghosszabb = név
        if len(legrövidebb) > len(név):
            legrövidebb = név

    for név in keresztnevek:
        for char in név:
            if char in betűk:
                betűk[char] += 1
            else:
                betűk[char] = 1

    legtöbbBetű = 'a'
    legtöbbBetűszáma = 0
    for (key, value) in betűk.items():
        if value > betűk[legtöbbBetű]:
            legtöbbBetű = key
            legtöbbBetűszáma = value

    print(f"Leghosszabb keresztnevek: {leghosszabb}")
    print(f"Legrövidebb keresztnevek: {legrövidebb}")
    print(f"Legtöbbet előforduló betű: {legtöbbBetű}, ennyiszer: {legtöbbBetűszáma}")


if __name__ == "__main__":
    main()
