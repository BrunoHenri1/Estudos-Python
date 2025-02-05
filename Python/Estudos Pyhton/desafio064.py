num = 0
cont = 0
soma = 0
num = int(input("Digite um numero [999 para finalizar!]:"))

while num != 999:    
    cont += 1
    soma += num
    num = int(input("Digite um numero [999 para finalizar!]:"))
print("Teve a entrada de {} numero e a soma deles é {}".format(cont, soma))
