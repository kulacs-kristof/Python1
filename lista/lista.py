def main() -> None:
    lista1: list[str] = ['marci', 'koppany', 'panyik']

    print(lista1[2])
    print(f'elemek: {len(lista1)}')

    for e in lista1:
        print(f'{e}, ', end='')
    print()

    print(lista1[0:0])

    for i, e in enumerate(lista1):
        print(f'{i} = {e}')
    print()

    # for i in range(len(lista1)):
    #    print(f'{i} = {lista1[i]}')

    lista1.append('balint')
    print(lista1)

    lista1.insert(0, 'kristóf')
    print(lista1)

    lista1.insert(2, 'brigi')
    print(lista1)

if __name__ == "__main__":
    main()
