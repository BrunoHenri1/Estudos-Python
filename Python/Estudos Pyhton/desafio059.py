from time import sleep
n1 = int(input("Digite o Primeiro numero: "))
n2 = int(input("Digite o Segundo numero: "))
opção = 0

while opção != 5:
    print(''' MENU DE ESCOLHA
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input("Qual sua escolha: "))
    sleep(1)

    if opção == 1:
        soma = n1 + n2
        print("A soma de {}+{}={}".format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print("A multiplicação de {}x{}={}".format(n1, n2, mult))
    elif opção == 3:
        if n1 > n2:
            print("Entre {} e {} o maior numero é {}".format(n1, n2, n1))
        else:
            print("Entre {} e {} o maior numero é {}".format(n1, n2, n2))
    elif opção == 4:
        n1 = int(input("Ok, digite novamente o primeiro numero:"))
        n2 = int(input("Digite novamente o segundo numero: "))
    elif opção == 5:
        print("Finalizando Programa...")
    else:
        print("Opção inválida")
sleep(1)
print("Fim do Programa!")
