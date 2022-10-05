from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
   
<<<<<<< HEAD
    return render(request, "ProyectoMujeresApp/home.html")
=======
    return render(request, "web/home.html")
>>>>>>> c2da2b72455eb1d56277cde350dd8b93d26fffa9


def institucional(request):
    
<<<<<<< HEAD
    return render(request, "ProyectoMujeresApp/institucional.html")



=======
    return render(request, "web/institucional.html")


def comunidad(request):
    
    return render(request, "web/comunidad.html")
>>>>>>> c2da2b72455eb1d56277cde350dd8b93d26fffa9


def comisiones(request):
    
<<<<<<< HEAD
    return render(request, "ProyectoMujeresApp/comisiones.html")

def usuario(request):
    
    return render(request, "ProyectoMujeresApp/usuario.html")

def logear(request):
    
    return render(request, "ProyectoMujeresApp/logear.html")


=======
    return render(request, "web/comisiones.html")
>>>>>>> c2da2b72455eb1d56277cde350dd8b93d26fffa9


def convenios(request):

<<<<<<< HEAD
    return render(request, "ProyectoMujeresApp/convenios.html")



=======
    return render(request, "web/convenios.html")


def contacto(request):

    return render(request, "web/contacto.html")
>>>>>>> c2da2b72455eb1d56277cde350dd8b93d26fffa9


