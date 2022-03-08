lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = input('Quer cotinuar? [S/N] ').lower()
    if resp != 's':
        print('-='*30)
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5  foi encontrado')
else:
    print('O valor 5 não está na lista')