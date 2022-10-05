from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
   
    return render(request, "ProyectoMujeresApp/home.html")


def institucional(request):
    
    return render(request, "ProyectoMujeresApp/institucional.html")





def comisiones(request):
    
    return render(request, "ProyectoMujeresApp/comisiones.html")

def usuario(request):
    
    return render(request, "ProyectoMujeresApp/usuario.html")

def logear(request):
    
    return render(request, "ProyectoMujeresApp/logear.html")




def convenios(request):

    return render(request, "ProyectoMujeresApp/convenios.html")





