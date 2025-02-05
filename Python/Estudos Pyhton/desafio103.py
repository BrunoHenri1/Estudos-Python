def ficha(Jog="<desconhecido>", gol=0):
    print(f"O Jogador {Jog} fez {gol} gol(s) no campeonato")



jogador = str(input("Nome do Jogador: "))
gols = str(input("Quantos gols feitos: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jogador.strip() == '':
    ficha(gol= gols)
else:
    ficha(jogador, gols)
