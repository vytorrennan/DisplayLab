from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")

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
