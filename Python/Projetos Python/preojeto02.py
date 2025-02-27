def lin():
    print("="*40)
def check(lista, lista2):

    msg = (f'{"Checklist do Dia":^40}')
    tam = len(msg)

    print("="*tam)
    print(msg)
    print("="*tam)

    a = ''
    for i in lista:
        while True:
            if a in "SIMNÃO":
                a = str(input(f"No dia de hoje {i}? ")).upper()
                lista2.append(a)
            
    lin()
    for k, j in zip(lista, lista2):    
        print(f"{k} --> {j}")
    lin()
    for i, j in zip(lista, lista2):
        if j == "NÃO":
            print(f"ENTÃO BORA {i.upper()}, ANDA!!!!")
    lin()
    

lista = ["Estudo", "Desenvolver", "Descansar"]
lista2 = list()
check(lista, lista2)

