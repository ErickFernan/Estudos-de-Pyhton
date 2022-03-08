from random import  randint
cont = 0
print('=-'*15,'\nVAMOS JOGAR PAR OU ÍMPAR','\n','=-'*15)
while True:
    x = int(input('Diga um valor: '))
    chute = input('Par ou Ímpar? [P/I] ').upper()
    pc = randint(0,10)
    soma = pc + x
    if soma % 2 == 0:
        resultado = 'DEU PAR'
    else:
        resultado = 'DEU IMPAR'
    print('-'*30,f'\nVocê jogou {x} e o computador {pc}. Total de {soma} {resultado}','\n','-'*30)
    if chute == resultado.strip()[4]:
        cont += 1
        print('Você VENCEU! \nVamos jogar novamente...','\n','=-'*15)
    else:
        print('Você PERDEU!','\n','=-'*15)
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break
