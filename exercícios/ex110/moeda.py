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


def resumo(n, a, d):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{d}% de redução: \t{diminuir(n, a, True)}')
    print('-' * 35)