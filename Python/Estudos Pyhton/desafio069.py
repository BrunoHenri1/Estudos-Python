quant_mulher = quant_homem = cont = 0


while True:
    idade = int(input("Qual a Idade? "))
    sexo = ' '
    
    while sexo not in "HM":
        sexo = str(input("Digite o Sexo: (H/M)")).upper() .split() [0]
    
    
    if idade >= 18:
        cont +=1
    if sexo == "H":
        quant_homem += 1
    if sexo == "M" and idade < 20:
        quant_mulher +=1
    
    contin = ' '
    while contin not in "SN":
        contin = str(input("Deseja Continuar?")).upper() .split() [0]
    if contin == "N":
        break
    
    
print(f'''A Quantidade de pessoas com mais de 18 anos é {cont}
No total tem {quant_homem} homens cadastrados
Mulheres a baixo de 20 anos tem {quant_mulher}''')