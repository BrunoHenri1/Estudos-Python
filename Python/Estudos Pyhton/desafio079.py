num = list()

while True:
    n = int(input("Digite um valor: "))
    if n not in num:
        num.append(n)
        print("Valor Adicionado com Sucesso")
    else:
        print("Numero ja foi digitado, não irei adicionar")

    
    resp = ' '
    while resp not in "SN":
        resp = str(input("Deseja Continuar? [S/N]")).upper() .strip() [0]
    if resp == "N":
        break
num.sort()
print(num)