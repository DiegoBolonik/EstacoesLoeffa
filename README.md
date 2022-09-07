# EstacoesLoeffa

<div align="center"> 
  <h1 align="center">Freelaway</h1>
</div>

<p align="center">
  <img alt="django" src="https://github.com/DiegoBolonik/EstacoesLoeffa/blob/main/Loeffa/project/static/django.png"><br>
  <img alt="001" src="https://github.com/DiegoBolonik/EstacoesLoeffa/blob/main/Loeffa/project/static/001.png" width=350>
  <img alt="002" src="https://github.com/DiegoBolonik/EstacoesLoeffa/blob/main/Loeffa/project/static/002.png" width=350>
  <img alt="003" src="https://github.com/DiegoBolonik/EstacoesLoeffa/blob/main/Loeffa/project/static/003.png" width=350>
  <img alt="004" src="https://github.com/DiegoBolonik/EstacoesLoeffa/blob/main/Loeffa/project/static/004.png" width=350>
</p>

## 🎯 Sobre

Resultado do teste técnico Loeffa. Cadastro de salas de trabalho. CRUD completo.

## 🚀 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

## ✅ Pré requisitos

Antes de começar 🏁, você precisa ter o [Python](https://www.python.org/downloads/) instalado em sua maquina.

## 🏁 Começando

1 - Primeiro clone o repositório e entre na pasta do projeto.

```bash
# Clone este repositório
$ git clone https://github.com/DiegoBolonik/EstacoesLoeffa
# Entre na pasta
$ cd EstacoesLoeffa
```

2 - Segundo inicie um ambiente virtual

```bash
# Criar
  # Linux
    $ python3 -m venv venv
  # Windows
    $ python -m venv venv
#Ativar
  # Linux
    $ source venv/bin/activate
  # Windows
    $ venv/Scripts/Activate
# Caso algum comando retorne um erro de permissão execute o código e tente novamente:
  $ Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

3 - Instale as dependências

```bash
# Instale as dependências
# Linux
$ pip3 install -r requirements.txt
# Windows
$ pip install -r requirements.txt
```

4 - Faça as migrações.

```bash
# Linux
python3 manage.py migrate
# Windows
python manage.py migrate
```

5 - Crie um super usuário

```bash
$ python3 .\manage.py createsuperuser
$ python .\manage.py createsuperuser
```

6 - Inicie a aplicação

```bash
# Para iniciar o projeto
# Linux
$ python3 manage.py runserver
# Windows
$ python manage.py runserver
# O app vai inicializar em <http://127.0.0.1:8000/>
# Para iniciar o projeto em uma porta especifica
$ python manage.py runserver <porta>
# O app vai inicializar em <http://127.0.0.1:<porta>/>
