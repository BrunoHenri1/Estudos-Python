from moeda import *


valor = float(input("Digite o valor: R$ "))

print(f"A metade de {valor} é {metade(valor)}")
print(f"O Dobro de {valor} é {dobro(valor)}")
print(f"O valor {valor} com 10% de desconto é {diminuir(valor, 10)}")
print(f"O valor {valor} com 10% de acréscimo é {aumentar(valor, 10)}")