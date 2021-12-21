def maior(*valores):
    print('-=' * 30)
    print('Analisando so valores passados...')
    if len(valores) != 0:
        mv = valores[0]
        for v in valores:
            print(f'{v}', end =' ')
            if mv < v:
                mv = v
    else:
        mv = 0
    print(f'Foram informados {len(valores)} ao todo.')
    print(f'O maior valor informado foi {mv}.')


# Início:
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

