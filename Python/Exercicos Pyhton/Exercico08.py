from time import sleep
while True:
    num = int(input("Digite um numero: [0 para finalizar]"))
    if num > 0:
        print("O numero é positivo!!")
    elif num < 0:
        print("O Numero é negativo!!")
    elif num ==0:
        print("Voce digitou 0, Finalizando programa")
        sleep(1)
        break
