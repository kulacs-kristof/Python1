# adott ax+b=0 egyenlet
# határozzuk meg a gyökét a és b ismeretlenek brkérése után
# a értékét kérjök újra ha a felhasználó 0-át ad

def egyenlet():
    print('Elsőfokú egyenlet ( ax + b = 0 ) megoldása (a != 0)')
    a: float = 0
    ismétel: bool = True
    while ismétel:
        a = float(input('a= ').replace(',', '.'))
        if a == 0:
            print('ne legyen 0')
            ismétel = True
        else:
            ismétel = False
    b = float(input('b= ').replace(',', '.'))
    print(f'x= {-b / a}')


egyenlet()
