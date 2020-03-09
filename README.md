# Cerbere-python

> Exemple d'intégration de [Cerbere](https://authentification.din.developpement-durable.gouv.fr) dans une application [Django](https://django.org)

## Installation du client CAS

Installation du client [django-cas-ng](https://djangocas.dev/):

```shell
pip install django-cas-ng
```

## Configuration du client CAS

Dans le fichier des [settings](cerbere/settings.py),

* ajouter le client cas dans les applis installées :

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cas_ng' # client cas
]
```

* ajouter le client cas dans les middlewares:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_cas_ng.middleware.CASMiddleware' # client cas
]
```

* ajouter le client cas dans les backends d'authentification:

```python
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend' # client cas
)
```

* ajouter la conf (url et version) du client CAS:

```python
# CAS config
CAS_SERVER_URL = 'https://authentification.din.developpement-durable.gouv.fr/cas/public'
CAS_VERSION = '2'
```

## Tests

```shell
pip install -r requirements.txt
python manage.py runserver
```

Lancez [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)

[Créer un compte Cerbère](https://authentification.din.developpement-durable.gouv.fr/authSAML/moncompte/creation/demande.do) si vous n'en avez pas.

**Seuls les sous-domaines du MTES-MCT autorisés, par exemple `.beta.gouv.fr`, `.e2.rie.gouv.fr` et `.developpement-durable.gouv.fr`, peuvent être utilisés.**

*Sinon vous aurez le message d'erreur au login: `Erreur à l'authentification. Adresse demandée invalide: ...`.*
