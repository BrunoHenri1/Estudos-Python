lista = []


while True:
    lista.append(int(input("Digite um valor: ")))
    resp = ' '
    while resp not in "SN":
        resp = str(input("Deseja Continuar? [S/N]")).upper() .strip() [0]
    if resp == "N":
        break

soma = sum(lista)

print(f"A média dos Valores é de {soma/len(lista)} ")