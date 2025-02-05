frase = str(input("Digite uma Frase: "))
espaço = 0

palavras = frase.split()
num_palavras = len(palavras)

print(f"A quantidade de palavras é {num_palavras}")

inverter = frase[::-1]
print(inverter)