from django.http import HttpResponse


def index(request):
    if request.user.is_authenticated:
        return HttpResponse('<p>Bienvenue dans <a href="https://github.com/MTES-MCT/cerbere-python">Cerbère démo</a>.</p><p>Vous êtes connecté en tant que <strong>%s</strong>.</p><p><a href="/accounts/logout">Déconnexion</a></p>' % request.user)
    else:
        return HttpResponse('<p>Bienvenue dans <a href="https://github.com/MTES-MCT/cerbere-python">Cerbère démo</a>.</p><p><a href="/accounts/login">Connexion</a></p>')