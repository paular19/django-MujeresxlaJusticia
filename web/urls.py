from django.urls import path

from web import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required 

urlpatterns = [
    path('', views.home, name="Home"),
    path('institucional', views.institucional, name="Institucional"),
    path('comisiones', views.comisiones, name="Comisiones"),
    path('convenios', views.convenios, name="Convenios"),
    # path('usuario', views.usuario, name="Usuario"),
    path('jurisp', login_required(views.jurisp), name="Jurisp"),
    path('pasaje', login_required(views.pasaje), name="pasaje"),
    path('clases', login_required(views.clases), name="clases"),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

