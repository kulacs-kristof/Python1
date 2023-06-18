print("LNKO kivonásos algoritmussal")

a = aT = int(input("a = "))
b = bT = int(input("b = "))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(f"LNKO({aT}, {bT}) = {a}")
