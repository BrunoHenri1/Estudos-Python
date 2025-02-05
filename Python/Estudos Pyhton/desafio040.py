nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Sua média é de {:.1f}, voce esta APROVADO!".format(media))
elif media >=5 and media < 7:
    print("Sua média é de {:.1f}, voce esta de RECUPERAÇÃO!!".format(media))
else:
    print("Sua média é de {:.1f}, voce esta REPROVADO!".format(media))