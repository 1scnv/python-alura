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



