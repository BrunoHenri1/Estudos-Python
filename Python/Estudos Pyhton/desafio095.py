time = []
jogador = {}
partidas = []

while True:
    jogador.clear()#Limpa o dict jogador pra começar o novo cadastro
    jogador['Nome'] = str(input("Nome do Jogador: "))
    jogos = int(input(f"Digite o total de partidas o {jogador['Nome']} teve: "))
    partidas.clear()
    for i in range(jogos):
        partidas.append(int(input(f"   Quantos gols na {i+1}° partida: ")))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())#Salva o jogador ja cadstrado

    while True:
        resp = str(input("Quer Continuar? [S/N]")).upper() [0]
        if resp in "SN":
            break
        print("ERRO! Responda apenas com S ou N")
    if resp == "N":
        break


print("=" * 40)
print("COD ", end='')

for i in jogador.keys():
    print(f"{i:<15}", end='')
print()

for k, v in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("=" * 40)

while True:
    busca = int(input("Mostrado dados de qual jogador: (999 encerra)"))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Não possui jogador com o código {busca}")
    else:
        print(f" -- Levantamento do Jogador {time[busca]['Nome']}:")
        for i, g in enumerate(time[busca]['Gols']):
            print(f"   No jogo {i+1} fez {g} gols")
        print('='*40)
print("Volte Sempre")