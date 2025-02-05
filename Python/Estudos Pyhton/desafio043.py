print("CALCULADORA DE IMC")
kg = float(input("Digite seu peso (Kg): "))
alt = float(input("Digite sua altura (m): "))

imc = kg / (alt ** 2)

print("O IMC dessa pessoa é de {:.2f}".format(imc))

if imc <= 16:
    print("Voce esta perigosamente a baixo do peso!")
elif imc <= 16.99:
    print("Voce esta a baixo do peso (Grave)")
elif imc <= 18.49:
    print("Voce esta abaixo do peso")
elif imc <= 24.99:
    print("Voce esta com o peso normal!")
elif imc <= 29.99:
    print("Voce esta com sobrepreso")
elif imc <= 34.99:
    print("Voce esta com obesidade grau I")
elif imc <= 39.99:
    print("VOce esta com obesidade grau II")
else: 
    print("Voce esta com Obesidade grau III! (Obesidade Mórbida)")