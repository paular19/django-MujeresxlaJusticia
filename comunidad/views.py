from django.shortcuts import render
from comunidad.models import Post

# Create your views here.

def comunidad(request):
    posts=Post.objects.all()
    return render(request, "comunidad/comunidad.html",{"posts":posts})