from random import randint
pc = randint (0, 10)
cont = 0

opção = int(input("Eu pensei em um numero entre 0 e 10, tente adivinhar qual é: "))

while opção != pc:
    opção = int(input("Errou, tente novamente: "))
    cont += 1
    if opção < pc:
        print("Mais... tente mais umas vez")
    elif opção > pc:
        print("Menos... Tente novamente")
print("Acertou, foi oq eu pensei")
print("Foram necessarios {} tentativas".format(cont))
