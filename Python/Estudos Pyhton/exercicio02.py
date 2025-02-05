gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

tot_joao = sum(gastos_joao)
tot_pedro = sum(gastos_pedro)

if tot_joao > tot_pedro:
    print("QUem Gastou mais foi o João")
elif tot_pedro > tot_joao:
    print("Quem gasotu mais foi Pedro")
else:
    print("Ambos gastaram a mesma quantidade")
