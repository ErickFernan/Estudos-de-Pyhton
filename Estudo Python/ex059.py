from time import sleep

val1 = int(input('Primeiro Valor: '))
val2 = int(input('Segundo Valor: '))

print('''      [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
opc = int(input('Qual é a sua opção? '))

while opc != 5:

    if opc == 1:
        soma = val1 + val2
        print('A soma entre {} + {} é {}'.format(val1,val2,soma))
        print('=-='*10)
        print('''        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
        opc = int(input('Qual é a sua opção? '))

    elif opc == 2:
        mult = val1 * val2
        print('A multiplicação entre {} + {} é {}'.format(val1, val2, mult))
        print('=-=' * 10)
        print('''        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
        opc = int(input('Qual é a sua opção? '))

    elif opc == 3:
        if val1 > val2:
            maior = val1
        else:
            maior = val2
        print('O maior nº entre {} e {} é {}'.format(val1, val2, maior))
        print('=-=' * 10)
        print('''        [ 1 ] somar
                [ 2 ] multiplicar
                [ 3 ] maior
                [ 4 ] novos números
                [ 5 ] sair do programa''')
        opc = int(input('Qual é a sua opção? '))

    else:
        print('Informe os número novamente: ')
        val1 = int(input('Primeiro Valor: '))
        val2 = int(input('Segundo Valor: '))
        print('=-=' * 10)
        print('''        [ 1 ] somar
                [ 2 ] multiplicar
                [ 3 ] maior
                [ 4 ] novos números
                [ 5 ] sair do programa''')
        opc = int(input('Qual é a sua opção? '))

print('Finalizando...')
sleep(1)
print('Fim do programa! Volte sempre!')
