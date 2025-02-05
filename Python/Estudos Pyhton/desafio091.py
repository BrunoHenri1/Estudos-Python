from random import randint
from time import sleep
from operator import itemgetter

sorteado = {'Jogador1': randint(1,6),
            'Jogador2': randint(1,6),
            'Jogador3': randint(1,6),
            'Jogador4': randint(1,6)}

ranking = list()

for k, v in sorteado.items():
    print(f"O {k} tirou {v} no dado!")
    sleep(1)

ranking= sorted(sorteado.items(), key=itemgetter(1), reverse = True)

print("Ranking de Jogadores")

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)    
