from django.urls import path

from ProyectoMujeresApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('institucional', views.institucional, name="Institucional"),
    path('comunidad', views.comunidad, name="Comunidad"),
    path('comisiones', views.comisiones, name="Comisiones"),
    path('convenios', views.convenios, name="Convenios"),
    path('contacto', views.contacto, name="Contacto"),
]