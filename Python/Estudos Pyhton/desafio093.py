jogador = {}
partidas = []
jogador['Nome'] = str(input("Nome do Jogador: "))
jogos = int(input(f"Digite o total de partidas o {jogador['Nome']} teve: "))

for i in range(jogos):
    partidas.append(int(input(f"   Quantos gols na {i+1}° partida: ")))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)

print("=-" * 30)
for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}")
print("=-" * 30)

print(f"O jogador {jogador['Nome']} teve um total de {jogos} partidas!")

print("=-" * 30)
for i, v in enumerate(jogador['Gols']):
    print(f"   ==>Na {i+1} partida ele fez {v} gols")

print(f'Foi um total de {jogador["Total"]} gols')
print("=-" * 30)