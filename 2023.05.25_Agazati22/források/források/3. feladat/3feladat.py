from toto import Fogadasi_fordulo

totok = []

def fileOlvas(file):
    with open(file, 'r', encoding='utf-8') as f:
        for sor in f.read().splitlines()[1:]:
            totok.append(Fogadasi_fordulo(sor.strip()))

def telitalalatok_szama():
    db = 0
    for t in totok:
        db += t.talalatok
    return db

def dontetlen_mentes():
    volt = False
    for t in totok:
        if 'X' not in t.eredmenyek:
            volt = True
            break
    return volt

fileOlvas('toto.txt')

print(len(totok))

print(telitalalatok_szama())

print(dontetlen_mentes())
