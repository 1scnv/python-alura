# API

## (App Programming Interface) Interface de programação de aplicações

- conjunto de regras, protocolos e ferramentas para comunicação de diferentes softwares
- padroniza troca de informações entre sistemas
- amplamente usadas para fornecer acesso a dados

-------------------
# TIPOS DE APIS

### API REST

- Utilizam protocolo HTTP para envio e recebimento de dados em JSON ou XML
- Segue arquitetura baseada em recursos e métodos HTTP(GET, POST, PUT, DELETE)

### API STREAMING -  
- permitem transmissão de dados em tempo real

----------------

# Classificação

### API Pública
Apis disponíveis para acesso livre sem autenticação ou autorização para acesso aos dados

### API Privada

API restrita e de acesso controlado, utilizadas por empresas para compartilhamento de dados internos com parceiros autorizados.
Necessário ter credencial de autenticação e autorização

---------


# Tipos de Requisições

### Get:
Utilizada com o objetivo de buscar informações de um servidor
Ex: consultar informações de um site

### Post:
utilizadas para enviar informações para o servidor
Ex: Criar um novo usuário ou enviar dados de um formulário

### Put:
utilizadas para substituir completamente um recurso no servidor
ex: Alterar informações do perfil em uma rede social

### Delete:
utilizada para excluir informações do servidor
Ex: Excluir um post em uma rede social


### Patch:

Utilizada para fazer alterações parciais em um recurso no servidor
Ex: Alterar apenas o status de uma tarefa em um sistema de gerenciamento de "Em andamento" para "Concluída"


---------

# Status Code

## 2xx (Sucesso)
Esses códigos indicam que a solicitação foi concludia com sucesso e o servidor está retornando os dados solicitados
Por exemplo, o código 200 indica que a solicitação foi bem-sucedida e que o servidor está retornando os dados solicitados.

## 3xx (Redirecionamento)
Esses códigos indicam que o cliente deve realizar mais ações para completar a solicitação.
Por exemplo, o código 301 indica que o servidor redirecionou a solicitação para uma nova URL permanente.

## 4xx (Erro do Cliente)
Esses códigos indicam que a solicitação não pode ser concluída devido a um erro no lado do cliente.
Por exemplo, o código 404 indica que a página solicitada não foi encontrada.

## 5xx (Erro do Servidor)
Esses códigos indicam que a solicitação não pôde ser concluída devido a um erro no lado do servidor.
Por exemplo, o código 500 indica que ocorreu um erro interno no servidor.

----------------------

# Parâmetros de requisições

## 1.Get:


### url:
- Url do recurso que deseja obter os dados. **Parâmetro obrigatório** e deve ser uma **string** contendo a URl a ser trabalhada

### params:
- Dicionário ou lista de tupla contendo os parâmetros de consulta a serem incluídos na URL<br>
Por exemplo, para fazer uma requisição GET para a API do Github e objer os repositórios de forma ordenada, pode-se passar o argumento
\
```params={”sort”: “name”}```
\
e ter os repositórios em ordem alfabética. Isso resultaria em uma URL como esta:
```https://api.github.com/users/Username/repos?sort=name```

### headers:
- Um dicionário contendo os cabeçalhos HTTP a serem enviados com a requisição. Os cabeçalhos podem ser usados, por exemplo, para enviar
informações de autenticação ou para definir o tipo de conteúdo esperado na resposta.

### auth:
- uma tupla contendo as credenciais de autenticação a serem usadas na requisição.
O primeiro elemento da tupla é o nome de usuário e o segundo é a senha.
Essa opção é usada quando a API requer autenticação.


### timeout:
- O tempo limite em segundos para aguardo da resposta da requisição.
Se a resposta não for recebida dentro do tempo limite a biblioteca gera um erro de tempo limite.

### verify:
- Um valor booleano (True ou False) que indica se deve ser verificado o certificado SSL da URL.
Se definido como True, a biblioteca verifica a validade.
Se definido como False, a biblioteca não verifica o certificado.

**O método GET é amplamente usado quando trabalhamos com APIs REST para obter informações de recursos específicos,
e a biblioteca Requests oferece muitas opções para personalizar a requisição e manipular a resposta.**


## 2. Post:

## 3. Put:

## 4. Delete:

## 5. Patch: