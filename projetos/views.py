from django.shortcuts import render
from .models import Projeto

# Create your views here.


def projetos(request):
    return render(request, "projetos.html")

def paginaDeProjeto(request, url):
    projeto = Projeto.objects.filter(url=url)
    context = {"projeto": projeto[0]}
    return render(request, "paginaDeProjeto.html", context)