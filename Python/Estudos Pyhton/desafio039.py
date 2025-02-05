from datetime import date
atual = date.today().year
ano = int(input("Ano de Nascimento: "))
sex = str(input("Voce é Homem ou Mulher: ")).strip().upper()

idade = atual - ano
alist = atual - (idade - 18)

if sex == "M":
    print("Voce não precisa se alistar!!")
elif sex == "H":
    print("Voce que nasceu em {} tem atualmente {} anos de idade".format(ano, idade))
    if idade > 18:
        print("Voce deveria ter se alistado em {}, ja passou {} anos desde então".format(alist, (atual - alist)))
    elif idade < 18:
        print("Voce vai se alistar em {}, ainda falta {} anos".format(alist, (alist - atual)))
    else:
        print("Voce deve se alistar nesse ano!")
else:
    print("Opção de sexo inválida. Por favor, insira 'H' para Homem ou 'M' para Mulher.")