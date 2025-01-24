def recebe_numero():
    numero = int(input('Digite um número inteiro: '))
    print(f'O número digitado foi: {numero}')
    return numero


def checa_numero(numero):
    if (numero % 2) == 0:
        print(f'O Número {numero} é par')
    else:
        print(f'O Número {numero} é ímpar')


def main():
    numero = recebe_numero()
    checa_numero(numero)
    exit()


if __name__ == '__main__':
    main()
