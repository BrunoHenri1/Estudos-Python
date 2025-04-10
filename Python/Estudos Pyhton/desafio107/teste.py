from moeda import *


valor = float(input("Digite o valor: R$ "))

print(f"A metade de R$ {valor:.2f} é R$ {metade(valor):.2f}")
print(f"O Dobro de R$ {valor:.2f} é R$ {dobro(valor):.2f}")
print(f"O valor R$ {valor:.2f} com 10% de desconto é R$ {diminuir(valor, 10):.2f}")
print(f"O valor R$ {valor:.2f} com 10% de acréscimo é R$ {aumentar(valor, 10):.2f}")