maior = menor = 0

for i in range (1,6):
    peso = float(input(f"Digite o Peso da {i}° pessoa: "))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(maior, menor)