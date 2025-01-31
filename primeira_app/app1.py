import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': True}
]


#['Pizza','Lasanha','Pastel','Sushi']

def nome_programa():

    print("""
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████───██████████████─████████████████──────██████████████─████████──████████─██████████████─████████████████───██████████████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████░░██─██░░██████░░██───██░░██████░░██─██░░████████░░██──────██░░██████████─████░░██──██░░████─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░██─────────██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─██░░██────██░░██──────██░░██───────────██░░░░██░░░░██───██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██─────────██░░██─────────
─██░░██████████─██░░██████░░██─██░░██████░░████─██░░██──██░░██─██░░████████░░██──────██░░██████████───████░░░░░░████───██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─────██░░░░░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████░░██─██░░██████░░██─██░░████████░░██─██░░██──██░░██─██░░██████░░████──────██░░██████████───████░░░░░░████───██░░██████████─██░░██████░░████───██░░██████████─██████████░░██─██████████░░██─
─────────██░░██─██░░██──██░░██─██░░██────██░░██─██░░██──██░░██─██░░██──██░░██────────██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────██░░██─────────────────██░░██─────────██░░██─
─██████████░░██─██░░██──██░░██─██░░████████░░██─██░░██████░░██─██░░██──██░░██████────██░░██████████─████░░██──██░░████─██░░██─────────██░░██──██░░██████─██░░██████████─██████████░░██─██████████░░██─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─██████──██████─████████████████─██████████████─██████──██████████────██████████████─████████──████████─██████─────────██████──██████████─██████████████─██████████████─██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n""")

def menu():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('clear')
    print('Finalizando App\n')
    exit()

def opcao_invalida():
    print('Opção Inválida\n')
    voltar_menu()

def exibir_subtitulo(texto):
    os.system('clear')
    print(f'{texto}\n')


def voltar_menu():
    input('Pressione ENTER para voltar ao menu...\n')
    main()


def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante: {nome_do_restaurante}:')
    dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu()


def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes cadastrados\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')
    voltar_menu()

def estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Digite o nome correto do restaurante')

    voltar_menu()



def opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        print(f"Voce escolheu a opcao: '{opcao_escolhida}'\n")

        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                estado_restaurante()
            case 4:
                finalizar_app()
                return
            case _:
                opcao_invalida()
    except ValueError:
        print("Opção inválida, por favor insira um número!\n")
        opcoes()

def main():
    os.system('clear')
    nome_programa()
    menu()
    opcoes()

if __name__ == '__main__':
    main()