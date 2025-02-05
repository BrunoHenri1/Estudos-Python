times = ("Botafogo", "Palmeiras", "Fortaleza", "Flamengo", "Internacional",
         "São Paulo", "Cruzeiro", "Bahia", "Corinthians", "Vasco da Gama",
         "Atlético-MG", "Vitória", "Grêmio", "Atlético-PR", "Juventude",
         "Fluminense", "Criciúma", "Bragantino", "Cuiabá", "Atlético-GO")

print("=" * 50)
print("Classificação da Tabela do Brasileirão: \n", times)
print("=" * 50)
print("Os 5 Primeiros Colocados são: \n",times[0:5])
print("=" * 50)
print("Os 4 ultimos colocados são: \n", times[-4:])
print("=" * 50)
print("Os times em ordem alfabética é: \n",sorted(times))
print("=" * 50)
print(f"O Cruzeiro esta no {times.index('Cruzeiro')+1}° posição")