print("=" * 30)
num = 0

while True:
    num = int(input("Digite um numero: "))
    if num < 0:
        break
    for i in range (0, 11):
        resul = num * i
        print(f'{num} x {i} = {resul}')
        
        
print("FIM")