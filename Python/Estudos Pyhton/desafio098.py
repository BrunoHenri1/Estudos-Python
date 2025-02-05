from time import sleep
def contador(i, f, p):
    print(f"Iniciando contagem de {i} a {f} de {p} em {p}")
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:    
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont+=p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont-=p
        print("FIM!")


#programa principal
contador(1,10,1)
contador(10, 0 , 2)
print("Escolha a forma da contagem")

ini = int(input("Digite o inicio da Contagem: "))
fim = int(input("DIgite o Fim da contagem: "))
passo = int(input("Digite o passo a passo: "))
contador(ini, fim, passo)