from datetime import date

atual = date.today().year
maior_idade = menor_idade = 0
mais_velho = mais_novo = 0

for geracao in range (1,8):
    ano = int(input(f"Digite o Ano em que a {geracao}° nasceu: "))
    if geracao == 1:
        mais_velho = ano
        mais_novo = ano
    else: 
        if ano < mais_velho:
            mais_velho = ano
        if ano > mais_novo:
            mais_novo = ano
    
    if atual - ano > 18:
        maior_idade += 1

    if atual - ano < 18:
        menor_idade += 1
print(f"Ao todo, tivemos {maior_idade} pessoas maiores de idade e o mais velho nasceu em {mais_velho}")
print(f"Tivemos {menor_idade} pessoas menores de idade e o mais novo nasceu em {mais_novo}")

