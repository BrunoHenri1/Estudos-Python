def leiaInt(num = 0):
  while True:
    try:
      num = int(input(num))
    except (ValueError, TypeError):
      print("\033[31mErro: Por favor Digite um numero inteiro.\033[m]")
      continue
    except KeyboardInterrupt:
      print("\033[31mEntrada de dados interrompida pelo usuario.\033[m")
      return 0
    else: 
      return num

def leiaFloat(num = 0):
  while True:
    try:
      num = float(input(num))
    except (ValueError, TypeError):
      print("\033[31mErro: Por favor Digite um numero Real.\033[m]")
      continue
    except KeyboardInterrupt:
      print("\033[31mEntrada de dados interrompida pelo usuario.\033[m")
      return 0
    else:
      return num

num = leiaInt('Digite um valor inteiro: ')
num1 = leiaFloat('Digite um valor real: ')
print(f'Voce acabou de digitar o numero inteiro {num} e o numero real {num1}')