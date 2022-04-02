from django.db.models import Model
from django.db.models.fields import TextField, CharField, EmailField, DateTimeField

class Usuario(Model):
    nombre_usuario=CharField(max_length=8)
    contraseña=CharField(max_length=12)
    correo=EmailField()

class Entrada(Model):
    titulo=CharField(max_length=20)
    texto=TextField()
    fecha=DateTimeField()

class Comentario(Model):
    usuario=Usuario.nombre_usuario
    texto=TextField()
    fecha=DateTimeField()




 