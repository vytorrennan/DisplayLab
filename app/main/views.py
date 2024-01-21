from django.views import View
from django.shortcuts import render
from . import models
from revista.models import Revista

# Create your views here.

class home(View):
    def get(self, request):
        carousel = models.carouselItem.objects.all()
        numItens = carousel.count()
        ultimosPosts = Revista.objects.filter(oculto=False).order_by("-edicao", "-dataHora")[0:4]
        context = {"carousel": carousel, "iterableNumItens": range(numItens), "ultimosPosts": ultimosPosts}
        return render(request, "home.html", context)


class institucional(View):
    def get(self, request):
        return render(request, "institucional.html")


class sobre(View):
    def get(self, request):
        membros = models.Membro.objects.filter(oculto=False)
        categorias = models.membroCategoria.objects.filter(oculto=False)
        context = {"membros": membros, "categorias": categorias}
        return render(request, "sobre.html", context)
