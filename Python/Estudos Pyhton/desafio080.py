num = list()

for i in range (0, 5):
    valor = int(input("Digite um valor: "))
    if i == 0 or valor > num[-1]:
        print("Adicionado ao Final da lista...")
        num.append(valor)
    else: 
        pos = 0
        while pos < len(num):
            if valor <= num[pos]:
                num.insert(pos, valor)
                print(f"adicionado na posição {pos} da lista...")
                break
            pos += 1
print("=" * 30)
print(f"Os valor Digitados em ordem foram {num}")