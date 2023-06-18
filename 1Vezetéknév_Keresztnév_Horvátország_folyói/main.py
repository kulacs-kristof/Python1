from River import River


def main() -> None:
# 4. feladat:
    rivers: list[River()] = []
    with open('HR_rivers.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            rivers.append(River(sor))

# 5. feladat:
    tenger_omol: int = 0
    for r in rivers:
        if 'Sea' in r.drain:
            tenger_omol += 1
    print(f'5. feladat: Tengerbe ömpő (torkolló) folyók száma: {tenger_omol}')

# 6. feladat:
    

main()