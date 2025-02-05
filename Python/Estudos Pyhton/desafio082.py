num = list()
par = list()
impar = list()
while True:
    num.append(int(input("Digite um valor: ")))

    resp = ' '
    while resp not in "SN":
        resp = str(input("Deseja Continuar? [S/N]")).upper() .strip() [0]
    if resp == "N":
        break

for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f"A lista Inteira: {num}")
print(f"A Lista só com os pares: {par}")
print(f"A Lista com impares: {impar}")
