# Projeto-F-brica

O presente projeto se trata de um desafio para os imersionistas da Fábrica de Software - UNIPÊ: criar um CRUD utilizando o Django Rest Framework. Sendo essa CRUD basead em uma clinica médica.

## Requisitos:

* asgiref==3.6.0
* Django==4.1.7
* djangorestframework==3.14.0
* psycopg2==2.9.5
* psycopg2-binary==2.9.5
* pytz==2023.3
* sqlparse==0.4.3
* tzdata==2023.3

### Criação Do Ambiente Virtual:

Inicialmente, foi criado ambiente virtual através do comando "py -m venv 'nome do ambiente virtual'", sendo seguido de sua ativação através de ".\'nome do ambiente virtual'\Scripts\activate.ps1". 

### Criação E Configuração do Projeto:

Por meio dos comandos "django-admin startproject 'nome do projeto' ." e "python manage.py startapp 'nome do app'", respectivamente, para criar o projeto e o aplicativo para a criação a API.

Após isso, deu-se inicio à configuração dos "models" ondem foram criadas as classes "Paciente" e "Consulta", definido os dados a serem armazenados.

Foram também configuradas as "views" para que fosse possível a execução das operações CRUD nos dados armazenados em cada model. Além da configuração dos "serializers", para que fosse possível a conversão dos dados.

Por fim, foi feita a configuração das "urls" para que seja possível o mapeamento das solicitações HTTP recebidas pelos clientes para as views correspondentes da sua API. 
