while True:
    num = int(input("Digite um numero: "))

    if num > 0:
        print("É um numero Positivo")
    elif num < 0:
        print("É um numero Negativo")
    else:
        print("É zero!")
    if num == 0:
        break
print("Programa Encerrado")