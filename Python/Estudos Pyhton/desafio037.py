num = int(input("Digite um numero para converter: "))
print('''Escolha qual sera a base de conversão:
[ 1 ] Binário 
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opcao = int(input("Seua opção: "))

if opcao == 1:
    print("{} convertido para binario é igual a {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para octal é igual a {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} convertido para Hexadecimal é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção invalida!!!")