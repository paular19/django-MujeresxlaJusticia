from django.urls import path

from web import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('institucional', views.institucional, name="Institucional"),
    path('comisiones', views.comisiones, name="Comisiones"),
    path('convenios', views.convenios, name="Convenios"),
    path('usuario', views.usuario, name="Usuario"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

