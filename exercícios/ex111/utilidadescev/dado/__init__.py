def leiaDinheiro(msg):
    msg = (input('Digite o preço: R$'))
    while msg is not msg.isnumeric():
        print(f'ERRO: "{msg}" é um preço inválido!')