ficha = list()

while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2:"))
    media = (nota1 + nota2) /2

    ficha.append([nome, [nota1, nota2], media])


    resp = ' '
    while resp not in "SN":
        resp = str(input("Deseja Continuar? [S/N]")).upper() .strip() [0]
    if resp == "N":
        break
    
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print("-"*26)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:>10}{a[2]:>8.1f}")

while True:
    opc = input("Deseja Saber quais as notas dos alunos (999 Interrompe)")
    if opc == 999:
        print("Finalizando")
        break
    if opc <= len(ficha) -1:
        print(f"Notas de {ficha[opc] [0]} são {ficha[opc] [1]}")
