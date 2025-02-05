num = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão: "))
termo = num
cont = 1

while cont <= 10:
    print("{} → ".format(termo), end='')
    termo += raz
    cont +=1
print("FIM")