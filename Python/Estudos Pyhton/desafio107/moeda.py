def aumentar(preço, taxa):
    porcent = (preço / 100) * taxa + preço
    return porcent

def diminuir(preço, taxa):
    diminui = preço - (preço / 100) * taxa
    return diminui

def dobro(preço):
    double = preço * 2
    return double

def metade(preço):
    meio = preço / 2
    return meio