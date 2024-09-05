from time import sleep
from random import randint

itens = ('pedra','Papel', 'Tesoura')
computador = randint(0, 2)
print('o computador escolheu {}'.format(itens[computador]))
print('''Suas opções: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogado?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
print("-=" * 10)
print('Computador Jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print("-=" * 10)
if computador == 0:
    if jogador == 0:
        print('EMPATE !!!')
    elif jogador == 1:
        print('VOCÊ VENCEU')
    elif jogador == 2:
        print('VITORIA do computador')
    elif jogador > 2:
        print('JOGADA INVÁLIDA!')     
elif computador == 1:
    if jogador == 0:
        print('VITORIA do computador')
    elif jogador == 1:
        print('EMPATE !!!')
    elif jogador == 2:
        print('VOCÊ VENCEU')
    elif jogador > 2:
        print('JOGADA INVÁLIDA!') 
elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('VITORIA do computador')
    elif jogador == 2:
        print('EMPATE !!!')
    elif jogador > 2:
        print('JOGADA INVÁLIDA!')     