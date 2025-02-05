from datetime import date
atual = date.today().year

pessoa = {}

pessoa['Nome'] = str(input("Nome: "))
pessoa['Ano'] = int(input("Qual ano de Nascimento: "))
pessoa['Carteira'] = int(input("Carteira de Trabalho: 0 (caso não tenha)"))

print("=-" *30 )

print(f"Nome: {pessoa['Nome']}")
print(f"Idade: ")
print(f"CTPS: {pessoa['Carteira']}")

if pessoa['Carteira'] != 0:
    pessoa['Contrato'] = int(input("Qual ano de contratação: "))
    pessoa["Salario"] = int(input("Salário: "))
    idade = atual - pessoa['Ano']
    print(f"Idade: {idade}")
    print(f"Salario: {pessoa['Salario']}")

