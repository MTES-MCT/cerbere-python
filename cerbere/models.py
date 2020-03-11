from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CerbereUserManager(BaseUserManager):
    def create_user(self, email, civilite, login, unite, first_name, last_name, password=None):
        """
        Creates and saves a CerbereUser with the given email, civilite, login, unite, first_name, last_name and password.
        """
        if not email:
            raise ValueError('Cerbere users must have an email address')
        if not login:
            raise ValueError('Cerbere users must have a login')
        if not unite:
            raise ValueError('Cerbere users must have an unite')
        if not civilite:
            raise ValueError('Cerbere users must have a civilite')
        if not first_name:
            raise ValueError('Cerbere users must have a first_name')
        if not last_name:
            raise ValueError('Cerbere users must have a last_name')

        user = self.model(
            email=self.normalize_email(email),
            civilite=civilite,
            login=login,
            unite=unite,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, civilite, login, unite, first_name, last_name, password=None):
        """
        Creates and saves a Cerbere superuser with the given email, civilite, login, unite, first_name, last_name and password.
        """
        user = self.create_user(
            email,
            password=password,
            unite=unite,
            civilite=civilite,
            login=login,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Create your models here.


class CerbereUser(AbstractBaseUser):
    uid = models.CharField(max_length=255, unique=True)
    civilite = models.CharField(max_length=255, blank=False)
    login = models.CharField(max_length=255, blank=False)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    unite = models.CharField(max_length=255, blank=False)
    siren = models.CharField(max_length=255, blank=True)
    tel_fixe = models.CharField(max_length=255, blank=True)

    objects = CerbereUserManager()

    USERNAME_FIELD = 'uid'
    REQUIRED_FIELDS = ['civilite', 'login', 'unite', 'first_name', 'last_name']


class Meta:
    app_label = "cerbere"
    db_table = "users"

    def __str__(self):
        return self.email

    def get_full_name(self):
        return '''%s %s''' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.login

    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_admin
