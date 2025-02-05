lista = ["Hamburguer", "Suco", "Pizza", "Sorvete"]

print(lista)
lista.append("Biscoito") #Adiciona o item na lista

print(lista)

lista.insert(0, "Cachorro-Quente") #adiciona o item no index que voc desejar
print(lista)

del lista[3]
lista.pop(3)#ambos os códigos retiram o item da lista

print(lista)

valores = [0, 5, 4, 3]

for i, c in enumerate(valores):
    print(f"na posição {i} encontrei o valor {c}")
    #A função enumerate() em Python é usada para obter índices e valores de uma lista de forma simultânea.