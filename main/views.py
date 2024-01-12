from django.shortcuts import render
from . import models
from revista.models import Revista

# Create your views here.


def home(request):
    carousel = models.carouselItem.objects.all()
    numItens = carousel.count()
    ultimosPosts = Revista.objects.filter(oculto=False).order_by("-edicao", "-dataHora")[0:4]
    context = {"carousel": carousel, "iterableNumItens": range(numItens), "ultimosPosts": ultimosPosts}
    return render(request, "home.html", context)


def institucional(request):
    return render(request, "institucional.html")


def sobre(request):
    membros = models.Membro.objects.filter(oculto=False)
    categorias = models.membroCategoria.objects.all()
    context = {"membros": membros, "categorias": categorias}
    return render(request, "sobre.html", context)


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
