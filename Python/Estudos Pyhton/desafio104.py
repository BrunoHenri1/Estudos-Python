def leiaInt(num):
    ok = False
    valor = 0
    while True:
        num = str(input("Digite um numero: "))
        if num.isnumeric():
            ok = True
            valor = num
            
        else:
            print("\033[0;33mERRO! Digite um valor Válido!\033[m")
        if ok:
            break
    return valor

#Programa Principal
n = leiaInt(" Digite um numero: ")
print(f"Voce digitou o numero {n}")