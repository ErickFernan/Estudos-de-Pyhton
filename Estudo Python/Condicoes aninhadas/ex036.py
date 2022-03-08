casa = float(input('Valor da casa? '))
salario = float(input('Valor do Salário? '))
tempo = float(input('Parcelas (\033[33mem anos\033[m)? '))

prestacao = casa/(tempo*12)
porc = prestacao/salario

if porc < 0.3:
    print('Parabéns! seu empréstimo foi aprovado e sua mensalidade será '
          'no valor de {:.2f} e ela corresponde a {:.2f}% de seu'
          'salário'.format(prestacao,porc))
else:
    print('Infelizmente seu empréstimo foi negado e sua mensalidade seria '
          'no valor de {:.2f} e ela corresponde a {:.2f}% de seu'
          'salário, o que ultrapassa os 30%'.format(prestacao, porc))