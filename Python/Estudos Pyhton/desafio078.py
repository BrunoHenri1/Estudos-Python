num = []
maior = menor = 0
for i in range(0,5):
    num.append(int(input(f"Digite um valor para a Posição {i}°: ")))
    if i == 0: 
        maior = menor = num[i]
    else:
        if num[i] > maior:
            maior = num[i]
        if num[i] < menor:
            menor = num[i]

print(num)
print(f"O Maior Numero digitado foi {maior} nas posições ", end='')
for c, v in enumerate(num):
    if v == maior:
        print(f'{c}...', end='')
print()
print(f"O Menor NUmero Digitado foi {menor} nas posições ", end='')
for a, m in enumerate(num):
    if m == menor:
        print(f"{a}...", end='')
print()