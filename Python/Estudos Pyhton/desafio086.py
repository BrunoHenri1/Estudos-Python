matr = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]

for l in range(0,3):
    for c in range(0,3):
        matr[l] [c] = int(input(f"Digite um Valor para [{l}], [{c}]"))
print("=-" * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matr[l][c]:^6}]", end='')
    print()