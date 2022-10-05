from django.urls import path

from .views import VUsuario, cerrar_sesion, logear


urlpatterns = [
   

    path('', VUsuario.as_view(), name="Usuario"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logear', logear, name="logear"),

]

