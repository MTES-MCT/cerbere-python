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
        <p>Vous êtes connecté en tant que <strong>%s</strong>.</p>
        <p><a href="/accounts/logout">Déconnexion</a></p>
         """ % request.user.username
    else:
        body = '<p><a href="/accounts/login">Connexion</a></p>'

    return HttpResponse(header + body + footer)

def ping(request: HttpRequest) -> HttpResponse:
    return HttpResponse('pong', content_type="text/plain")