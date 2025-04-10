from moeda import *


valor = float(input("Digite o valor: R$ "))

print(f"A metade de R$ {moeda.valor} é R$ {metade(valor)}")
print(f"O Dobro de R$ {moeda.valor} é R$ {dobro(valor)}")
print(f"O valor R$ {moeda.valor} com 10% de desconto é R$ {diminuir(valor, 10)}")
print(f"O valor R$ {moeda.valor} com 10% de acréscimo é R$ {aumentar(valor, 10)}")