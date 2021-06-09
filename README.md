
<h1 align="center">Aplicação SimpleMOOC do curso em vídeo com Django </h1>
<p align="center">
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#information_source-como-executar">Como executar</a>&nbsp;&nbsp;&nbsp;
</p>
<p align="center"><img src="https://raw.githubusercontent.com/LeandroSimo/agenda/master/kisspng-django-python-computer-icons-logo-portable-network-django-python-recruitment-task-1-5b6748f386f486.9191155715334955395528.png" align="" ></p>

## :rocket: Tecnologias

Esse aplicação foi desenvolvida com as seguintes tecnologias:
- [Python][python]
- [Django3][django]


## :information_source: Como executar

Para clonar e executar essa aplicação você precisará do [Git](https://git-scm.com) + [Python][python] + [Django][django] instalados no seu computador.

### Clone e execute 

```bash
# Clone esse repositório
$ git clone https://github.com/LeandroSimo/simplemooc-curso-django.git

# Entre no repositório
$ cd simplemooc-curso-django/

# Crie a virtuallenv
No Windows:
$ python -m venv venv

No macOS ou Linux:
$ python3 -m venv venv

# Ative a virtuallenv
No Windows:
$ cd env
$ cd Scripts
$ activate
.\env\Scripts\activate

No macOS ou Linux:
$ cd env
$ cd bin
$ activate
source env/bin/activate

# Instale o Django 
$ pip install Django

# Execute
$ cd curso
$ python manage.py runserver


```
#### PS.: Atentem-se em instalar as dependências no arquivo [requirements.txt][requeriments] e criar o Banco de Dados com o superuser

```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver ou python manage.py runserver 0.0.0.0:8000
```

[python]: https://www.python.org/downloads/
[django]:https://www.djangoproject.com/download/
[requeriments]: https://github.com/LeandroSimo/curso-django/blob/main/requirements.txt
