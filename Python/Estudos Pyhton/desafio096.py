def area(larg, compr):
    a = larg * compr
    print(f"A area de um tererro com {larg}x{compr} = {a}m²")


print("Calculando Area")
print("=-" *20)
l = int(input("Digite a largura: "))
c = int(input("Digite o comprimento: "))

area(l,c)