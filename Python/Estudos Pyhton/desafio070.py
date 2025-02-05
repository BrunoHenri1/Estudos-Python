print("Cadastrando produtos")
menor = maior = tot_gasto = cont = 0
barato = ' '


while True:
    produto = str(input("Qual o nome do Produto: "))
    preço = float(input("Qual o Preço do Produto: "))
    tot_gasto += preço
    cont += 1
    if preço >= 1000:
        maior += 1
    
    if cont == 1:
        menor = preço
        barato = produto
    else: 
        if preço < menor:
            menor = preço
            barato = produto

    contin = ' '
    while contin not in "SN":
        contin = str(input("Deseja Continuar? ")).upper() . split() [0]
    if contin == "N":
        break
print(f'''O total gasto foi de {tot_gasto}
No total teve {maior} com valor maior que R$1000,00
O Menor valor é R${menor:.2f} e foi {barato}''')