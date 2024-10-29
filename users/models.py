from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Redefinicion o sobreescritura de la clase user
class User(AbstractUser):
    # Modificaciones para usar el email como herramienta de autenticacion principal en vez del username
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []