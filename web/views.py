from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
   
    return render(request, "web/home.html")


def institucional(request):
    
    return render(request, "web/institucional.html")


def comunidad(request):
    
    return render(request, "web/comunidad.html")


def comisiones(request):
    
    return render(request, "web/comisiones.html")


def convenios(request):

    return render(request, "web/convenios.html")


def contacto(request):

    return render(request, "web/contacto.html")


