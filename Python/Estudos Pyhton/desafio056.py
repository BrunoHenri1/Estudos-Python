somaidade = 0
maior_idadeH = 0
mais_velho = ''
mulheres = 0
for i in range (1, 5):

    nome = str(input("Digite o Nome da {}° Pessoa: ".format(i))).upper().strip()
    idade = int(input("Qual a idade: "))
    sexo = str(input("Qual o sexoo? (M/F):")).upper().strip()

    somaidade += idade
    if i == 1 and sexo == "M":
        maior_idadeH = idade
        mais_velho = nome
    if sexo == "M" and idade > maior_idadeH:
        maior_idadeH = idade
        mais_velho = nome

    if sexo == "F":
        if idade < 20:
            mulheres += 1


media = somaidade / 4
print("A média de idade do grupo de pessoas é {}". format(media))
print("O Homem mais velho tem {} anos e se chama {}".format(maior_idadeH, mais_velho)) 
print("O total de mulheres a baixo de 20 anos é de {}".format(mulheres))
    