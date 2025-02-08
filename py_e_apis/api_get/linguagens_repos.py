import requests

r = requests.get('https://api.github.com/versions') # armazena a requisição em uma variável

# print(r) # printa a variável com o retorno da requisição

print(r.status_code) # retorna apenas o código do status do retorno armazenado na variável

# print(r.url) # retorna a URL acessada

# r.text # retorna o texto completo do acesso a api

print(r.json()) # retorna o json correspondente ao acesso a api
