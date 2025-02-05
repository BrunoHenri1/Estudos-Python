matr = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
som = maior = colu= 0

for i in range(0,3):
    for j in range(0,3):
        matr[i] [j] = int(input(f"Digite um Valor para [{i}], [{j}]"))
print("=-" * 30)
for i in range (0,3):
    for j in range (0,3):
        print(f"[{matr[i][j]}]", end='')
        if matr [i] [j] %2 ==0:
            som += matr[i] [j]
    print()

print(f"A Soma dos Valores Pares é {som}")

for i in range (0,3):
    colu += matr[i][2]

print(f"A soma da terceira coluna é {colu}")

for j in range (0,3):
    if j == 0:
        maior = matr[1] [j]
    elif matr [1] [j] > maior:
        maior = matr [1] [j]
print(f"O maior numero da segunda coluna é {maior}")