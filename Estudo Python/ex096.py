def área(larg, comp):
    total = larg * comp
    print(f'A área de um terreno {l} x {c} é de {total}m².')


# programa principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)