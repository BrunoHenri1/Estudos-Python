import urllib
import urllib.request

try:
  site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
  print("O site Pudim não esta acessivel")
else:
  print("Consegui Acessar o site pudim")
  print(site.read()) #comando que mostra o HTML do site