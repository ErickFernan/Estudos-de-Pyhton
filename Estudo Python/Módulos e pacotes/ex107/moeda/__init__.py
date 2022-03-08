def metade(v=0, frmat=False):
    m = v/2
    return m if frmat is False else moeda(m)


def dobro(v=0, frmat=False ):
    m = v*2
    return m if not frmat else moeda(m)


def aumentar(v=0, tx=0, frmat=False):
    m = v + v * tx/100
    return m if frmat is False else moeda(m)


def diminuir(v=0, tx=0, frmat=False):
    m = v - v * tx/100
    return m if frmat is False else moeda(m)


def moeda(v, moeda='R$'):
    frmt = f'{moeda}{v:.2f}'.replace('.', ',')
    return frmt


def resumo(v=0, a=10, d=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":}'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado:"} \t{moeda(v)}')
    print(f'{"Dobro do preço:"} \t{dobro(v, True)}')
    print(f'{"Metade do preço:"} \t{metade(v, True)}')
    print(f'{a}% de aumento: \t{aumentar(v, a,True)}')
    print(f'{d}% de redução: \t\t{diminuir(v, d,True)}')
    print('-' * 30)