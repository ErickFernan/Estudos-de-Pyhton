lista = []
while True:
    var = int(input('Digite um valor: '))
#    if lista.count(var) == 0:
    if var not in lista:
        lista.append(var)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resposta = input('Quer continuar? [S/N] ')
    if resposta.lower() != 's':
        break
print('=-'*30)
lista.sort()
print(f'Você digitou os valores {lista}')