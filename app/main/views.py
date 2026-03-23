from django.views import View
from django.shortcuts import render
from . import models
from revista.models import Revista
from coletar_noticias.models import NoticiaExterna


class home(View):
    def get(self, request):
        carousel = models.carouselItem.objects.all()
        numItens = carousel.count()
        ultimosPosts = Revista.objects.filter(oculto=False).order_by("-edicao", "-dataHora")[0:3]
        
        noticias_sbc = NoticiaExterna.objects.filter(fonte='SBC').order_by('-data_publicacao')[0:10]
        noticias_games = NoticiaExterna.objects.filter(fonte='CRITICAL_HITS').order_by('-data_publicacao')[0:10]
        context = {
            "carousel": carousel,
            "iterableNumItens": range(numItens),
            "ultimosPosts": ultimosPosts,
            "noticias_sbc": noticias_sbc,
            "noticias_games": noticias_games
        }

                   
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
    
class parceiros(View):
    def get(self, request):
        return render(request, "parceiros.html")