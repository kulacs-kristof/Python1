from VbEredmeny import VbEredmeny


def main() -> None:
    eredmények: list[VbEredmeny] = []
    with open('fociVBk.csv', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            eredmények.append(VbEredmeny(sor))

    print(f'1. feladat: Csapatok száma: {len(eredmények)}')

    print('\n2. feladat: 2018-as VB csapatai:')
    kiírt_országok_száma: int = 0
    # HF: Minta szerinti kiírás egyszerűbb algoritmussal
    for e in eredmények:
        if e.utolsó_év == 2018:
            if kiírt_országok_száma == 0:
                print('\t', end='')
            elif kiírt_országok_száma % 4 == 0:
                print('\n\t', end='')
            print(f'{e.ország:14}', end='')
            kiírt_országok_száma += 1

    benelux_alkalom: int = 0
    for e in eredmények:
        # if e.ország == 'Belgium' or e.ország == 'Hollandia' or e.ország == 'Luxemburg':
        if e.ország in ['Belgium', 'Hollandia', 'Luxemburg']:
            benelux_alkalom += e.részvételek_száma
    print(f'\n\n3. feladat: A BeNeLux országok összesen {benelux_alkalom} alkalommal vettek részt a VB-n')

    # 4. feladat:
    első_év: int = eredmények[0].első_év
    for e in eredmények[1:]:
        if e.első_év < első_év:
            első_év = e.első_év
    print(f'\n4. feladat: Az első VB-t {első_év}-ban rendezték')

    # 5. feladat:
    bajnok_db: int = 0
    for e in eredmények:
        if e.legjobb_eredmény_rövid == 'Világbajnok':
            bajnok_db += 1
    print(f'\n5. feladat: Eddig {bajnok_db} ország csapata volt világbajnok')


if __name__ == "__main__":
    main()
