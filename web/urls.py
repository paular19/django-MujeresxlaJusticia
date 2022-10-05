from django.urls import path

<<<<<<< HEAD
from ProyectoMujeresApp import views
from django.conf import settings
from django.conf.urls.static import static
=======
from web import views
>>>>>>> c2da2b72455eb1d56277cde350dd8b93d26fffa9

urlpatterns = [
    path('', views.home, name="Home"),
    path('institucional', views.institucional, name="Institucional"),
    path('comisiones', views.comisiones, name="Comisiones"),
    path('convenios', views.convenios, name="Convenios"),
    path('usuario', views.usuario, name="Usuario"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

