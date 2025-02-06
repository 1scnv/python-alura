import requests

base_url = 'https://api.github.com'
owner = 'amzn'
url = f'{base_url}/users/{owner}/repos'
access_token = '<token>'
headers ={
    'X-Github-Api-Version':'2022-11-28',
    'Authorization':'Bearer ' + access_token
}
print(f'A URL é:{url}')

response = requests.get(url, headers=headers)
print(f'O resultado da requisição é: {response.status_code}')

#print(len(response.json()))

repos_list=[]
for page_num in range(1,6):
    try:
        url_page = f'{url}?page={page_num}'
        response = requests.get(url_page, headers=headers)
        repos_list.append(response.json())
    except:
        repos_list.append(None)

#print(len(repos_list))
#print(len(repos_list[0]))

#print(repos_list[0][1]['name'])

repos_name = []

for page in repos_list: # laco para acessar as paginas
    for repo in page: #laco para acessar os repositorios dentro das paginas
        repo['name'] # pega o nome do repo
        repos_name.append(repo['name']) #adiciona o repo na variavel repos_name

print(repos_name)
#print(len(repos_name))

print(repos_list[1][1]['language'])

repos_language = []
for page in repos_list:
    for repo in page:
        repo['language']
        repos_language.append(repo['language'])
