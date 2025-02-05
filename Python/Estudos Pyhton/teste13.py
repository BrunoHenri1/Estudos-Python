estado = {}
brasil = []

for cont in range(0, 3):
    estado['uf'] = input("Unidade Federativa: ")
    estado['sigla'] = input("Sigla do Estado: ")
    #.copy serve como um fatiamento da lista
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    for key, value in e.items():
        print(f"O Campo {key} tem valor {value}")