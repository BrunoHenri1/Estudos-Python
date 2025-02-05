resp = "S"
media = 0
soma = 0
quant = 0
maior = 0
menor = 0

while resp in "Ss":
    num = int(input("Digite um numero: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N] ")).upper().strip() [0]
media = soma / quant
print("O Maior numero que voce digitou foi {} e o menor foi {}".format(maior, menor))
print("Voce digitou {} numeros e a média foi {}".format(quant, media))
