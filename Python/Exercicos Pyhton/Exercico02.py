#Verificar se um número é par ou ímpar: Desenvolva um programa que receba um número como entrada e determine se ele é par ou ímpar.

num = int(input("Digite um Numero: "))

if num % 2 ==0:
    print(f"O numero {num} é par")
else:
    print(f"o numero {num} é impar")