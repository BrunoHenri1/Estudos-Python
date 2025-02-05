num = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão: "))
termo = num
cont1 = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont1 <= total:
        print("{} → ".format(termo), end='')
        termo += raz
        cont1 +=1
    print("Pausa")
    mais = int(input("Quantos termos a mais voce quer mostrar? "))
print("Fim")
print("Total de termos utilizados {}".format(total))