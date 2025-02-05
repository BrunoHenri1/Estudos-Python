def maior(*num):
    cont = maior = 0
    print("Analisando os valores passados", end=' ')

    for valor in num:
        print(f"{valor}", end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"E o maior e {maior}")

maior(0,2,9,1)