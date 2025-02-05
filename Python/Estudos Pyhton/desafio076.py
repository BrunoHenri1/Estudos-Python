print("=" * 40)
print("{:^40}" .format("Lista de Preços"))
print("=" * 40)

listagem = ("Lapis", 1.56,
            "Borracha", 2,
            "Caderno",15.9,
            "Estojo", 25,
            "Transferidor", 4.2,
            "Compasso", 9.99,
            "Mochila", 120.32,
            "Canetas", 22.3,
            "Livro", 34.9)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f"{listagem[item]:.<30}", end="")
    else:
        print(f"RS{listagem[item]:>7.2f}")