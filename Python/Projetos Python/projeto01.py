from time import sleep
dados = [[], []]

print("=-"*10)
print("Lojinha do Bruno")
print("=-"*10)

while True:
    opc = str(input("Deseja Salvar como cliente ou produtos [C/P/N]: ")). upper()

    if opc == "C":
        dados[0].append(str(input("Digite o Nome do Cliente: ")))
    elif opc == "P":
        dados[1].append(str(input("Digite o Produto: ")))
    elif opc == "N":
        break
    else:
        print("Opção inválida")
print("=-"*10)        
sleep(1)

while True:
    opc = int(input('''O que deseja ver
1 - Clientes Cadastrados
2 - Produtos Cadastrados
3 - Finalizar Programa\n'''))
    print("Buscando informações")
    print("=-"*10)
    sleep(1)

    if opc == 1:
        for indicie, item in enumerate(dados[0]):
            print(indicie, item)
        print("=-"*10)
    elif opc == 2:
        for indicie, item in enumerate(dados[1]):
            print(indicie, item)
        print("=-"*10)
    elif opc == 3:
        break
    else:
        print("Opção Inválida")

print("Programa Finalizado")