from django.shortcuts import render
from links.models import Links


# Create your views here.

def links(request):
    posts=Links.objects.all()
    return render(request, "links/links.html",{"posts":posts})
