num = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a Razão: "))
deci = num + (10-1) * raz

for i in range (num, deci+raz, raz):
    print(i ,end=" → ")
print("FIM")