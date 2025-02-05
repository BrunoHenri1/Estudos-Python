print("=-"*15)
print("{:^30}".format("Caixa Eletronico"))
print("=-"*15)
valor = int(input("Digite o Valor que quer Sacar: "))
ced = 50
total_ced = 0
total = valor

while True:
    if total >= ced:
        total -= ced
        total_ced +=1
    else:
        if total_ced > 0:
            print(f"O total de {total_ced} cedulas de R$ {ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        total_ced = 0
        if total == 0:
            break
print("=-" * 15)