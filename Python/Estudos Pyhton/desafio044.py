from time import sleep

print("Formas de pagamento")

valor = float(input("Valor das compras: "))

print('''FORMAS DE PAGAMENTO: 
[ 1 ] a vista dinheiro/cheque 
[ 2 ] a vista no cartão 
[ 3 ] parcelado (Até 4x sem juros)''')

opcao = int(input("Selecione a opção: "))
print("Processando...")
sleep(2)

if opcao == 1:
    descon1 = valor - (valor * 10 / 100)
    print("Calculando...")
    sleep(2)
    print("Sua compra foi no valor de R${:.2f}, pagando a vista voce ganha 10% de desconto, ficando o total da sua compra de R${:.2f}".format(valor, descon1))
elif opcao == 2:
    descon2 = valor - (valor * 5 / 100)
    print("Calculando...")
    sleep(2)
    print("Sua compra foi no valor de R${:.2f}, pagando avista no cartão voce ganha 5% de desconto, ficando o total da sua compra de R${:.2f}".format(valor,descon2))
elif opcao == 3:
    parce = int(input("Em quantas vezes voce quer parcerlar: "))
    if parce <= 4:
        print("Calculando...")
        sleep(2)
        print("Sua compra não teve juros, então ficou {} parcelas de R${:.2f}, o total da sua compra foi de R${}".format(parce, valor/parce, valor))
    else:
        print("Calculando...")
        sleep(2)
        juros = valor+ (valor * 20/100)
        print("Sua compra teve juros de 20%, então ficou {} parcelas de R${:.2f}!, o total da sua compra foi de R${}".format(parce, juros/parce, juros))
else:
    print("Opção inválida!")