num = (int(input("DIgite um numero: ")),
        int(input("DIgite um numero: ")),
        int(input("DIgite um numero: ")),
        int(input("DIgite um numero: ")))
print(f"Voce digitou os numero: {num}")
print(f"O Valor 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O Numero 3 apareceu na {num.index(3)+1}° posição")
else:
    print("O valor 3 não foi digitado")
print("Os valores digitados pares foram", end=" ")

for n in num:
    if n % 2 ==0:
        print(n, end=" ")
