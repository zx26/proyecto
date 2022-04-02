from abc import abstractmethod
from rest_framework.viewsets import ModelViewSet
from blog.serializers import UsuarioSerializador, EntradaSerializador, ComentarioSerializador

class VistaBase(ModelViewSet):
    """Resumen  
    

    
    Clase padre de las vistas api view, cuya finalidad es servir
    de herencia para las demas que esten en el proyecto"""

    serializer_class=None #variable de la clase del serializador declarada none por su uso abstracto
    

    filterset_fields = '__all__'

    search_fields = ['name']

    ordering_fields = '__all__'

    def get_queryset(self):
        """Metodo que designara y retornara el query sin 
        tener que tocar nada en las demas clases"""
        
        model= self.get_serializer().Meta.model
        queryset=model.objects.filter()
        return queryset     


    @classmethod
    def get_view_set(self):
        return self

    @abstractmethod
    def __str__(self):
        pass       

class ApiUsuario(VistaBase):
    serializer_class=UsuarioSerializador

    def __str__(self):
        return r"usuario"

class ApiEntrada(VistaBase):
    serializer_class=EntradaSerializador

    def __str__(self):
        return r"entrada"

class ApiComentario(VistaBase):
    serializer_class=ComentarioSerializador 

    def __str__(self):
        return r"comentario"

class ApiViewGeneral(object):

    def __init__(self) -> None:
        super().__init__()
        self.viewset= [ApiUsuario(),ApiEntrada(),ApiComentario(),]


    def get_view_set(self):
        return self.viewset                   