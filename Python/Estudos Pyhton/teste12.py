print("=-"*30)
pessoas = {"nome": "Bruno", "Sexo": "M", "idade": "25"}
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")

pessoas['peso'] = 90.0
for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k,v in pessoas.items():
    print(f"{k} = {v}")
print("=-"*30)

brasil= []
estado1 = {"UF": "Paraná", "Sigla": "PR"}
estado2 = {"UF": "São Paulo", "Sigla": "SP"}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['Sigla'])