from django.shortcuts import render

# Create your views here.
from jurisp.models import Jurisp


def jurisp(request):
    posts=Jurisp.objects.all()
    return render(request, "jurisp/jurisp.html",{"posts":posts})