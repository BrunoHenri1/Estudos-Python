from datetime import date
atual = date.today().year
cont1 = 0
cont2 = 0

for i in range(1, 8):
    ano = int(input("Digite o ano que a {} pessoa nasceu: ".format(i)))
    idade = atual - ano

    if idade >= 18:
        cont1 += 1
    else:
        cont2+= 1
print("A quantidade de pessoas MAIORES de idade são {}".format(cont1))
print("A quantidade de pessoas MENORES de idade são {}".format(cont2))
