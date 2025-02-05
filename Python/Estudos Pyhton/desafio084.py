lista_temporaria = list()
principal = list()
maior = menor = 0

while True:
    lista_temporaria.append(str(input("Digite o nome:")))
    lista_temporaria.append(float(input("Digite o Peso: ")))
    if len(principal) == 0:
        maior = menor = lista_temporaria[1]
    else:
        if lista_temporaria[1] > maior:
            maior = lista_temporaria[1]
        if lista_temporaria[1] < menor:
            menor = lista_temporaria[1]

    principal.append(lista_temporaria[:])
    lista_temporaria.clear()

    resp = str(input("Deseja COntinuar? [S/N]")).upper() .strip() [0]
    if resp == "N":
        break


print("=-" * 30)
print(f"Ao todo voce cadastrou {len(principal)} pessoas")
print(f"O maior Peso foi {maior} de ", end='')
for p in principal:
    if p[1] == maior:
        print(f"{p[0]}", end=' ')
print()
print(f"O menor peso foi {menor} de", end='')
for p in principal:
    if p[1] == menor:
        print(f"{p[0]}", end='')
print()