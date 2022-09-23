from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
   
    return render(request, "ProyectoMujeresApp/home.html")


def institucional(request):
    
    return render(request, "ProyectoMujeresApp/institucional.html")


def comunidad(request):
    
    return render(request, "ProyectoMujeresApp/comunidad.html")


def comisiones(request):
    
    return render(request, "ProyectoMujeresApp/comisiones.html")


def convenios(request):

    return render(request, "ProyectoMujeresApp/convenios.html")


def contacto(request):

    return render(request, "ProyectoMujeresApp/contacto.html")


