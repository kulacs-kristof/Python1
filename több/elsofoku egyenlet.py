# Elsőfokú egyenlet megoldása
# Adott ax+b=0 egyenlet
# Határozzuk meg a gyökét az a és b ismeretlenek (valós) bekérése után
# A értékét kérjük újra ha a felhasználó 0át ad
# x = -(b/a)

from random import randint


def main() -> None:
    print("Elsőfokú egyenlet megoldása! ax+b=0")
    '''
    a = float(input("a = "))
    while a == 0:
        a = float(input("a = "))
        print("Az a nem lehet 0!")
    b = float(input("b = "))
    x = -(b / a)
    print(f"x={x}")
    '''

    
def egyenlet_megoldó(együttható1: str, együttható2: str) -> float:
    # 10 db együttható string generálása véletlenszerűen és tárolása
    # Az a értéke nem lehet nulla
    # a = valós szám [-300; +300]
    # b = valós szám [-250; + 123]
    # Irjuk ki az egyenlet megoldásait


if __name__ == "__main__":
    main()
