sexo = str(input("Qual seu Sexo? [M/F] ")).upper().strip() [0] # o 0 depois do strip serve para pegar somente a primeira letra

while sexo not in "MF":
    sexo = str(input("Dados inválidos. Informe uma opção válida:")).strip().upper()
print("Sexo {} registrado com sucesso".format(sexo))
   
