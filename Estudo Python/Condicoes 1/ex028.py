import random
from time import sleep
n = int(random.uniform(0, 6))
print(n)
sleep(5)
chute = int(input('Digite um chute inteiro entre 0 e 5: '))
print('Você acertou!' if chute == n else 'Você errou!')



