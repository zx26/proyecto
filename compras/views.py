from django.http import HttpRequest
from django.views import View

class Vista(View):
     def get(self, request):
          return HttpRequest("Proyecto web modificado, buenos dias")