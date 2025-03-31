def notas(*n, sit = False):
  """notas = r esse "r" era um parametro na minha tentativa
  cont = 0
  maior = menor = 0

  for i in notas:
    if cont == 0:
      maior = i
      menor = i
    if cont > 0:
      if i > maior:
        maior = i
      if i < menor:
        menor = i
    cont +=1
    media = sum(r)/ cont
    dicio = {"Total": cont, "Maior": maior, "Menor": menor, "Média": media}
    """
  r = dict()
  r['total'] = len(n)
  r['maior'] = max(n)
  r['menor'] = min(n)
  r['media'] = sum(n)/len(n)
  if sit:
    if r['media'] >= 7:
      r['situação'] = "Boa"
    elif r["media"] >= 5:
      r['situação'] = "Razoavel"
    else:
      r['situação'] = "Ruim"
  
  
  return r

resp = notas(5, 5, 10, 10, sit=False)
print(resp)