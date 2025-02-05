num = list()
cont = 0
while True:
    num.append(int(input("Digite um valor: ")))
    resp = ' '
    while resp not in "SN":
        resp = str(input("Deseja Continuar? [S/N]")).upper() .strip() [0]
        cont += 1
    if resp == "N":
        break
print(f"Voce DIgitou {cont} elementos")
if 5 in num:
    print("O Valor 5 foi encontrado!")
else:
    print("O valor 5 não foi encontrado")

print(f"A lista em ordem DECRESCENTE: {sorted(num, reverse=True)}")


