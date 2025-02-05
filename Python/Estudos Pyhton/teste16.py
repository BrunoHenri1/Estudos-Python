pessoas = {'Nome': "Bruno", 'Sexo': 'M', 'Idade': 22}
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['Sexo']
pessoas['Nome'] = 'Jose'
pessoas['Peso'] = 98.5

for k, v in pessoas.items():
    print(f"{k} = {v}")

print('=-' * 30)

brasil = list()
estado1 = {'UF': "Rio de Janeiro", 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0] ['UF']) 

print('=-' * 30)

pais = list()
Estados = dict()

for c in range(0,3):
    Estados['UF'] = str(input("Unidade Federativa: "))
    Estados['Sigla'] = str(input("Sigla do Estado: "))
    pais.append(Estados.copy())
for e in pais:
    for valor in e.values():
        print(valor, end=' ')
    print()
        