def metade(n, formato = False):
    n = n / 2
    return n if formato is False else moeda(n)


def dobro(n, formato = False):
    n = n * 2
    return n if formato is False else moeda(n)


def aumentar(n, a, formato = False):
    n = (n * (100 + a)) / 100
    return n if formato is False else moeda(n)


def diminuir(n, d, formato = False):
    n = (n * (100 - d)) / 100
    return n if formato is False else moeda(n)

def moeda(n = 0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
