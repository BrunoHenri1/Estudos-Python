num = soma = cont = 0

while True:
    num = int(input("Digite um valor    [999 para finalizar]: "))
    if num == 999:
        break
    cont += 1
    soma += num
    
print(f'Foi digitado {cont} e a soma deles foi {soma}')