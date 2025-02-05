frase = str(input("Digite uma Frase: ")).strip() .upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print("o Inverso de {} é {}".format(junto, inverso))

if inverso == junto:
    print("É um Palindromo")
else:
    print("Não é um Palindromo")