def fatorial(n, show = False):
    """
    --> Calcula Fatorial de um numero
    :param n: O numero a ser calculado
    :param show: mostra o calculo feito para realizar o fatorial
    :return: retorna o valor calculado
    
    """
    f = 1
    for i in range (n, 0,-1):
        if show:
            print(i, end='')
            if i > 1:
                print(f" x ", end='')
            else:
                print(" = ", end='')
        f *= i
    return f
        
        


print(fatorial(5, show= True))
