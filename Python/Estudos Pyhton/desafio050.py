soma = 0
cont = 0

for i in range (1, 7):
    num = int(input("Coloque o {}° valor: ".format(i)))
    if num % 2 == 0:
        soma += num
        cont += 1
print("A soma dos numeros é {} e tem {} numeros pares".format(soma, cont))
