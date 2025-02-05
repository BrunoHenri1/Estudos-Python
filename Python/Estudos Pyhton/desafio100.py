from random import randint
from time import sleep

def sorteio(lista):
    print("\nSorteando 5 valores...", flush=True)
    sleep(1)
    for i in range (0,5): 
        a = randint(0,9)  
        lista.append(a)
        print(f"{a}", end=' ', flush=True)
        sleep(0.5)
    print("FIM")

def somar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares temos o resultado {soma}")


numeros = list()
sorteio(numeros)
somar(numeros)
print(numeros)