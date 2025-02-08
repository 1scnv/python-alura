import requests

url = 'https://api.github.com/users/1scnv'

response = requests.get(url)

print(f'Resposta da requisição: {response.status_code}\n')

print(f'Nome da conta requisitada: {response.json()["name"]}')
print(f'Nome de Usuário: {response.json()["login"]}')
print(f'Repositórios Públicos: {response.json()["public_repos"]}')
print(f'Data de criação da conta: {response.json()["created_at"]}')