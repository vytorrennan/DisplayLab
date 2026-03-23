from django.views import View
from django.shortcuts import render
from .models import NoticiaExterna


class NoticiaView(View):
    def get(self, request):
        return render(request, "noticias/home.html")


class ListaNoticias(View):
    def get(self, request):
        noticias_sbc = NoticiaExterna.objects.filter(fonte='SBC')
        noticias_games = NoticiaExterna.objects.filter(fonte='CRITICAL_HITS')

        context = {
            'noticias_sbc': noticias_sbc,
            'noticias_games': noticias_games,
            'title': 'Lista de Notícias'
        }

        return render(request, "noticias/home.html", context)