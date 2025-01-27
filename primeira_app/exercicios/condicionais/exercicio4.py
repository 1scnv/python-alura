def main():
    x, y = recebe_coordenadas()
    plano_cartesiano(x,y)
    exit()

def recebe_coordenadas():
    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))
    return x,y

def plano_cartesiano(x,y):
    match(x, y):
        case (x, y) if x > 0 and y > 0:
            print('Primeiro Quadrante: os valores de x e y devem ser maiores que zero;')
        case (x, y) if x < 0 and y > 0:
            print('Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;')
        case (x, y) if x < 0 and y < 0:
            print('Terceiro Quadrante: os valores de x e y devem ser menores que zero;')
        case (x, y) if x > 0 and y < 0:
            print('Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;')
        case _:
            print('Caso contrário: o ponto está localizado no eixo ou origem.')

if __name__ == "__main__":
    main()