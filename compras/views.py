from django.http import HttpRequest, HttpResponse
from django.views import View

class Vista(View):

    def __init__(self, **kwargs) -> None:
      super().__init__(**kwargs)

    def get(self, request):
          return HttpResponse('Proyecto web modificado, buenos dias')