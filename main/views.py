from django.shortcuts import render
from . import models

# Create your views here.


def home(request):
    carousel = models.carouselItem.objects.all()
    numItens = carousel.count()
    context = {"carousel": carousel, "iterableNumItens": range(numItens)}
    return render(request, "home.html", context)

def institucional(request):
    return render(request, "institucional.html")

def sobre(request):
    return render(request, "sobre.html")


#temporarios-------

def displayCast(request):
    return render(request, "postsProjetos/displayCast.html")

def exterminandoDrogas(request):
    return render(request, "postsProjetos/exterminandoDrogas.html")

def peruacuDigital(request):
    return render(request, "postsProjetos/peruacuDigital.html")

def educaRedes(request):
    return render(request, "postsProjetos/educaRedes.html")

#------------------
