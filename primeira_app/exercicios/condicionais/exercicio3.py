def main():
    usuario = recebe_usuario()
    senha = recebe_senha()
    checa_senha(senha,usuario)
    exit()

def checa_senha(senha,usuario):
    usuario_cadastrado = 'admin'
    senha_cadastrada = '12345'
    if senha == senha_cadastrada and usuario == usuario_cadastrado:
        print(f"""Login realizado com sucesso\n"{usuario_cadastrado}" seja bem vindo ao sistema.""")
    else:
        print('A senha e/ou o usuário estão incorretos.')
    

    
def recebe_usuario():
    usuario = input('Digite seu usuario: ')
    return usuario
    
def recebe_senha():
    senha = input('Digite sua senha: ')
    return senha


if __name__ == '__main__':
    main()