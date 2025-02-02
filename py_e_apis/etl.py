import requests

headers = {'X-Github-Api-Version':'2022-11-28'}
base_url = 'https://api.github.com'
owner = 'amzn'
url = f'{base_url}/users/{owner}/repos'
print(f'A URL é:{url}')


response = requests.get(url, headers=headers)
print(f'O resultado da requisição é: {response.status_code}')

print(len(response.json()))
