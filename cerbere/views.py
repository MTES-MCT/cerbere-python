from django.http import HttpRequest, HttpResponse
from . import signals

def index(request: HttpRequest) -> HttpResponse:
    header = '''<!DOCTYPE html>
<html>
  <head>
    <title>Démo Cerbère avec Django</title>
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
  </head>
  <body>
  <h1>Bienvenue dans cerbere-python demo</h1>'''

    footer = '''
    <hr><p><a href="https://github.com/MTES-MCT/cerbere-python/">Code source</a></p>
  </body>
</html>'''

    if request.user.is_authenticated:
      body = """
      <p>Vous êtes connecté en tant que <strong>%s. %s %s</strong>.</p>
      <p>Login: %s</p>
      <p>Email: <a href="mailto:%s">%s</a></p>
      <p>Tél fixe: %s</p>
      <p>Unité: %s</p>
      <p><a href="/accounts/logout">Déconnexion</a></p>
        """ % (request.user.civilite, request.user.first_name, request.user.last_name, request.user.login, request.user.email, request.user.email, request.user.tel_fixe, request.user.unite)
    else:
        body = '<p><a href="/accounts/login">Connexion</a></p>'

    return HttpResponse(header + body + footer)

def ping(request: HttpRequest) -> HttpResponse:
    return HttpResponse('pong', content_type="text/plain")