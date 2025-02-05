palavra = ("Cereja","mercado","mercado", "cerveja", "acerola","Banana")
for p in palavra:
    print(f"\nNa palavra {p.upper()} temos ", end=" ")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")