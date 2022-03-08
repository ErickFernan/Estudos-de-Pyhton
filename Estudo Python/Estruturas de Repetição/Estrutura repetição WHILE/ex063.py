print('_'*50,'\nSequência de Fibonacci')
print('_'*50)
termos = int(input('Quantos termos você quer mostrar? '))
print('~'*50)
cont = ant = 0
atual = 1
print('0 → ',end='')
while cont < termos - 1:
    soma = ant + atual
    print(atual, end=' → ')
    ant = atual
    atual = soma
    cont += 1
print('FIM')
print('~'*50)