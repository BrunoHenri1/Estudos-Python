from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)

print('''===JOKEPO===
Escolha sua opção!
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

player = int(input("Qual sua escolha? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")


print('-=' * 20)
print("O Computador escolheu {}".format(itens[pc]))
print("Voce escolheu {}".format(itens[player]))
print('-=' * 20)

if pc == 0:
    if player == 0:
        print("Deu EMPATE!")
    elif player == 1:
        print("O Player Ganhou!!")
    elif player == 2:
        print("A Maquina Ganhou!")
    else: 
        print("JOGADA INVALIDA")
elif pc == 1:
    if player == 0:
        print("A Maquina Ganhou!")
    elif player == 1:
        print("Deu EMPATE!")
    elif player == 2:
        print("O Player Ganhou!")
    else: 
        print("JOGADA INVALIDA")
elif pc == 2:
    if player == 0:
        print("O Player Ganhou!")
    elif player == 1:
        print("A Maquina Ganhou!")
    elif player == 2:
        print("Deu EMPATE")
    else: 
        print("JOGADA INVALIDA")