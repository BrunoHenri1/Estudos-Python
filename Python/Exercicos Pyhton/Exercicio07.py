#Escreva um programa que receba uma frase do usuário e conte quantas palavras ela possui. Em seguida, inverta a ordem das palavras na frase.
frase = str(input("Digite uma Frase: ")).split()

print(f"A Frase contém {len(frase)} palavras!")
print(f"A Frase de trás pra frente é {frase[::-1]}")
