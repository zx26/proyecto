from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, EmailField

class Usuario(Model):
    "Modelo para registrar datos de Usuarios"

    usuario= CharField(max_length=20)
    correo= EmailField(max_length=30) 