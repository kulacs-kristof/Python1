import random

jatekos1 = input("Első játékos neve: ")
jatekos2 = input("Második játékos neve: ")

jelenlegijatekos = ""

körszám = 0
dobás1 = 0
dobás2 = 0

while dobás1 + dobás2 != 12:

    if jelenlegijatekos == jatekos1:
        jelenlegijatekos = jatekos2
    else:
        jelenlegijatekos = jatekos1

        körszám += 1
        print(f"{körszám}.kör:")

    dobás1 = random.randint(1, 6)
    dobás2 = random.randint(1, 6)
    print(f"{jelenlegijatekos} dobása: {dobás1} + {dobás2}")

print(f"A játékot {jelenlegijatekos} kezdheti")
