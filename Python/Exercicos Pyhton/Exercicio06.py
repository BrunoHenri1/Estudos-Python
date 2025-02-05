num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

while True:
    print("=-" *30)
    opc = int(input('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR '''))

    if opc == 1:
        a = num1 + num2
        print(f"Voce escolheu SOMA, e a soma dos numeros {num1} + {num2} = {a}")

    elif opc == 2:
        b = num1 * num2
        print(f"VOce escolheu MULTIPLICAR, e o resultado entre {num1} X {num2} = {b}")

    elif opc == 3:
        if num1 > num2:
            print(f"O Primeiro numero é maior! {num1}")
        else:
            print(f"O Segundo numero é o maior! {num2}")
    elif opc == 4:
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite outro numero: "))
    elif opc == 5:
        break
    elif opc > 5:
        print("Opção Inválida")
print("FIm do Programa")
