num = int(input("Digite um numero: "))
cont = 0

for i in range(1, num+1):
    if num % i == 0:
        print("\33[34m", end='')
        cont += 1
    else:
        print("\33[31m", end='')
    print(i, end=' ')
print("\n\033[mO número {} foi divisível {} vezes!".format(num, cont))
if cont == 2:
    print("É Um numero primo!")
else:
    print("Não é um numero primo!")