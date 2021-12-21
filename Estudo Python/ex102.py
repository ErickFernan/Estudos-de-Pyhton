def fatorial(n, show=False):
    """n = Obrigatório, valor de entrada para fazer o fatorial
       Show = Opcional, mostra as contas
       return = fatorial ou fatorial + contas
    """
    fat = 1
    if show:
        for i in range(1, n + 1):
            fat *= i
            print(f'{i}', end='')
            if i != n:
                print(' x ', end='')
        print(f' = {fat}')

    else:
        for i in range(1, n + 1):
            fat *= i
        print(fat)


# ínicio
fatorial(5, True)
help(fatorial)
