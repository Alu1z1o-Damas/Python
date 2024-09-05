from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?'))
print('Processando...')
sleep(3)
if jogador == computador:
    print('PARABÊNS! Você conseguiu me vencer!')
else:
    print('ERROU! Eu pensei no número {} e não no {}!'.format(computador, jogador))
