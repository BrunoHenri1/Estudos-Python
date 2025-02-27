from time import sleep

print("="*30)
print(f"{'Cajan Embalagens':^30}")
print("="*30)

usuario = "Bruno"
password = '123'
produtos = []

while True:
  login = str(input("Login: "))
  senha = str(input("Senha: "))
  if login != usuario or senha != password:
    print("Usuario incorreto")
  else:
    break
sleep(1)
print("=" * 30)
print(f"{'MENU':^30}")
print("=" * 30)
while True:
  produto = str(input("Produto: "))
  preço = float(input("Preço R$: "))
  produtos.append((produto, preço))
  resp = ' '
  while resp not in "SN":
    resp = str(input("Deseja continuar cadastrando produtos? [S/N]")).upper().strip()[0]
  if resp == "N":
    break
print("="*30)
print(f"{'Produtos':^30}")
print("="*30)

for produto, preço in produtos:
  print(f"{produto:<21}", end='')
  print(f"R${preço:7.2f}")