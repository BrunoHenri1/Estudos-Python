dados = {}
lista = []
soma = media = 0

while True:
    dados.clear()
    dados['Nome'] = str(input("Nome: "))
    while True:
        dados['Sexo'] = str(input("Sexo: [M/F] ")).upper() [0]
        if dados["Sexo"] in 'MF':
            break 
        print("ERRO!! Por favor Digite somente M ou F")
    dados['Idade'] = int(input("Idade: "))
    soma += dados["Idade"]
    lista.append(dados.copy())

    while True:
        resp = str(input("Deseja COntinuar? [S/N]")).upper() [0]
        if resp in "SN":
            break
        print("ERRO!!! Digite apenas S ou N!")
    if resp == "N":
        break
print("=-" * 30)
print(f"A) Ao todo temos {len(lista)} pessoas cadastradas")

media = soma / len(lista)
print(f"B) A média de idade é de {media} anos")
print(f"C) As mulheres cadastradas foram ", end='')

for p in lista:
    if p["Sexo"] == "F":
        print(f"{p['Nome']} ", end='')
    

print("D) Lista das pessoas que estão acima da média de idade")

for p in lista:
    if p["Idade"] > media:
        print(f"   Nome = {p['Nome']}; Sexo = {p['Sexo']}; Idade = {p['Idade']}")
