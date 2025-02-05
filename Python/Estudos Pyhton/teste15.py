lista = ["Spotify", "Youtube", "Netflix", "Dinsey+"]


for indicie, item in enumerate(lista):
    print(f"{indicie} {item}")

opc = int(input("Digite qual app voce deseja abrir: "))

print(f"Abrindo {lista[opc]}")
