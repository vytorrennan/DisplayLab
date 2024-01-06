from django.shortcuts import render

# Create your views here.


def projetos(request):
    return render(request, "projetos.html")
