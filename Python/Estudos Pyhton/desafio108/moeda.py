def aumentar(preço=0, taxa=0):
    porcent = (preço / 100) * taxa + preço
    return porcent


def diminuir(preço=0, taxa=0):
    diminui = preço - (preço / 100) * taxa
    return diminui


def dobro(preço=0):
    double = preço * 2
    return double


def metade(preço=0):
    meio = preço / 2
    return meio


def moeda(preço=0, moeda="R$"):
    return f"{moeda}{preço:>.2f}".replace('.',',')