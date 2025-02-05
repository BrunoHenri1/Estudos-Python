#dados = dict() ou dados = {}

dados = {'nome': "Pedro", 'idade': "25"}

print(dados["nome"])
print(dados["idade"])

#adicionando elementos

dados ["sexo"] = "M"

print(dados["sexo"])

#Deletando elementos

del dados["idade"]

print("=-" *30)

filme= {"titulo": "Star Wars",
        "ano": "1977",
        "diretor": "George Lucas"
        }

#retorna os valores
print(filme.values())
#retorna as chaves 
print(filme.keys())
#retorna valores e chaves
print(filme.items())

print("=-"*30)

for k,v in filme.items():
    print(f"o {k} é {v}")