from random import randint
v = 0

while True: 
    player = int(input("Digite um numero de 0 a 10: "))
    pc = randint(0, 10)
    total = player + pc
    tipo = ' '

    while tipo not in "PI":
        tipo = str(input("Par ou Impar?")).upper().split()[0]
    print(f'Voce escolheu {player} e a maquina {pc} e total foi {total}')

    if tipo == "P":
        if total % 2 == 0:
            print("Voce Ganhou!")
            v +=1
        else:
            print("Voce Perdeu")
            break

    elif tipo == "I":
        if total % 2 == 1:
            print("Voce Ganhou!")
            v += 1
        else:
            print("Voce Perdeu!")
            break
    print("Vamos Jogar Novamente...")
print(f"Voce venceu {v} vezes")