def main():
    idade = recebe_idade()
    classifica_idade(idade)
    exit()


def recebe_idade():
    idade = int(input('Digite sua idade: '))
    print(f'A sua idade é: {idade}')
    return idade

def classifica_idade(idade):
    match idade:
        case idade if 0 <= idade <= 12:
            print('Criança: 0 a 12 anos')
        case idade if 13 <= idade <= 18:
            print('Adolescente: 13 a 18 anos')
        case _:
            print('Adulto: acima de 18 anos')




if __name__ == '__main__':
    main()