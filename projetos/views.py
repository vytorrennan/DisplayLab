from django.shortcuts import render
from .models import Projeto

# Create your views here.


def projetos(request):
    projeto = Projeto.objects.all()
    context = {"projeto": projeto }
    return render(request, "projetos.html", context)

def paginaDeProjeto(request, url):
    projeto = Projeto.objects.filter(url=url)
    context = {"projeto": projeto[0]}
    return render(request, "paginaDeProjeto.html", context)