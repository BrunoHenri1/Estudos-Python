palavras = ["python", "asimov", "código", "web", "programação"]

maior_palavra = palavras[0]
menor_palavra = palavras[0]

for letras in palavras:
    if len(letras) > len(maior_palavra):
        maior_palavra = letras
    if len(letras) < len(menor_palavra):
        menor_palavra = letras
print(f"A menor palavra é {menor_palavra}")
print(f"A maior palavra é {maior_palavra}")