fluxo_caixa = []

print("=" * 15)
print("{:^15}".format("Fluxo Caixa"))
print("=" * 15)
print('''1 -- Adicionar Receita
2 -- Adicionar Despesa
Digite outro numero para encerrar!''')

def info():
    nome = str(input("Digite seu Nome: "))
    valor = int(input("DIgite o Valor: "))
    fluxo_caixa.append({
        "nome": nome,
        "valor": valor
    })

while True:
    opcao = int(input("QUal opção: "))

    if opcao == 1:
        info()
    elif opcao == 2:
        info()
    else:
        break
total = 0
for nf in fluxo_caixa:
    print("nome: ", nf["nome"], ", Valor: R$:", nf["valor"])
    total += nf["valor"]

print("Saldo Atual é de:", total)