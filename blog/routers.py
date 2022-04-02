from rest_framework.routers import DefaultRouter
from blog.views import ApiViewGeneral
router=DefaultRouter()

api_principal= ApiViewGeneral()

for viewset in api_principal.get_view_set():
    router.register(viewset.__str__(), viewset.get_view_set(), basename=viewset.__str__() )

urlpatterns=router.urls