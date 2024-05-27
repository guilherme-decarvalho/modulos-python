def metade(n = 0):
    n = n / 2
    return n


def dobro(n = 0):
    n = n * 2
    return n


def aumentar(n = 0, a = 0):
    n = (n * (100 + a)) / 100
    return n


def diminuir(n = 0, d = 0):
    n = (n * (100 - d)) / 100
    return n


def moeda(n = 0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')