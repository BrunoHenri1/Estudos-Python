

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 15:
        return f"Com {idade} não é obrigatório Votar"
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} o voto é opcional"
    else:
        return f"Com {idade} anos é ORIGATÓRIO votar"
    
ano = int(input("Digite o ano de Nascimento: "))
print(voto(ano))