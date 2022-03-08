vel = float(input('Velocidade do carro: '))
if vel > 80:
    print('Você recebeu uma multa de {} reais.'.format(int((vel-80)*7)))
else:
    print('Siga seu caminho')
