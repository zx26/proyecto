from rest_framework.serializers import ModelSerializer
from blog.models import Usuario, Entrada, Comentario

class UsuarioSerializador(ModelSerializer):
    class Meta:
        model=Usuario
        fields='__all__'        

class EntradaSerializador(ModelSerializer):
    class Meta:
        model=Entrada
        fields='__all__'  

class ComentarioSerializador(ModelSerializer):
    class Meta:
        model=Comentario
        fields='__all__'  