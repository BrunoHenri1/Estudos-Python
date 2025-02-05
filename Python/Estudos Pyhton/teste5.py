resp = "S"
soma = quant = média = maior = menor = 0

while resp in "Ss":
    num = int(input("DIgite um Numero: "))
    soma+= num
    quant += 1

    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


    resp = str(input("Quer continuar? S/N ")).upper() .strip() [0]
print(f'O menor numero foi {menor} e o maior foi {maior}')
print("Acabou")