import math


a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

diszkriminans = (b**2) - 4 * a * c

if diszkriminans < 0:
    print("Nincs megoldás")
    exit()
elif diszkriminans == 0:
    print("Egy megoldás")
else:
    print("Két megoldás")

gyok1 = (-b + math.sqrt(diszkriminans)) / (2 * a)
gyok2 = (-b - math.sqrt(diszkriminans)) / (2 * a)

print("\tx =", gyok1)

if gyok1 != gyok2:
    print("\ty =", gyok2)
