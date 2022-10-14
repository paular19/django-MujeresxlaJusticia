from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
   
    return render(request, "web/home.html")


def institucional(request):
    
    return render(request, "web/institucional.html")

def links(request):
    
    return render(request, "web/links.html")










def comisiones(request):
    
    return render(request, "web/comisiones.html")

# def usuario(request):
    
#     return render(request, "web/usuario.html")

def login(request):
    
     return render(request, "web/login.html")




def convenios(request):

    return render(request, "web/convenios.html")

@login_required
def jurisp(request):

    return render(request, "web/jurisp.html")




@login_required
def pasaje(request):
    return render(request, "web/pasaje.html")

@login_required
def clases(request):

    return render(request, "web/clases.html")





