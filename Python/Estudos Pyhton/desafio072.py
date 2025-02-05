num = ("zero", "um", "dois", "três", "quatro",
       "cinco", "seis", "sete", "oito", "nove",
       "dez", "onze", "DOZE", "treze", "quartorze",
       "quinze", "dezeseis", "dezesete", "dezoito",
       "dezenove", "vinte")

while True:
    opcao = int(input("Digite um numero de 0 a 20: "))
    if 0 <= opcao < 20:
        break
    opcao = int(input("Numero Inválido. Digite um numero SOMENTE entre 0 e 20: "))

    resp = num[opcao]

    print(f"o numero por Extenso é: {resp}")

    pausa = str(input("Quer continuar? [S/N] ")). upper() .strip() [0]
    while pausa not in "SN":
        pausa = str(input("Opção invalida! DIgite [S/N]: ")). upper() .strip() [0]
    if pausa == "N":
        break
print("Acabou")
    
    