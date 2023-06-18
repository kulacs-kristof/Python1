def LNKO(a, b):
    # Két pozitív egész szám legkisebb közös többszöröse, az a legkisebb pozitív egész szám, amelynek minkét szám osztója
    nsz = 0
    ksz = 0
    osztando = 0

    if a > b:
        nsz = a
        ksz = b
    else:
        nsz = b
        ksz = a

    osztando = nsz

    while osztando % ksz != 0:
        osztando += nsz
    return osztando
