from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms.novoItemCarousel import novoItemCarouselForm
from .forms.novoProjeto import novoProjetoForm
from .forms.novoPostRevista import novoPostRevistaForm
from .forms.novoMembro import novoMembroForm
from .forms.novaCategoriaDeMembro import novaCategoriaDeMembroForm

# Create your views here.
@login_required
def contentManagement(request):
    return render(request, "contentManagement.html")


@login_required
def novoProjeto(request):
    context = {}
    if request.method == "POST":
        context['form'] = novoProjetoForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'] = "Não valido!"
    else: 
        context['form'] = novoProjetoForm()
    return render(request, "novoProjeto.html", context)


@login_required
def novoItemCarousel(request):
    context = {}
    if request.method == "POST":
        context['form'] = novoItemCarouselForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'] = "Não valido!"
    else: 
        context['form'] = novoItemCarouselForm()
    return render(request, "novoItemCarousel.html", context)


@login_required
def novoPostRevista(request):
    context = {}
    if request.method == "POST":
        context['form'] = novoPostRevistaForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'] = "Não valido!"
    else: 
        context['form'] = novoPostRevistaForm()
    return render(request, "novoPostRevista.html", context)


@login_required
def novoMembro(request):
    context = {}
    if request.method == "POST":
        context['form'] = novoMembroForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'] = "Não valido!"
    else: 
        context['form'] = novoMembroForm()
    return render(request, "novoMembro.html", context)


@login_required
def novaCategoriaDeMembro(request):
    context = {}
    if request.method == "POST":
        context['form'] = novaCategoriaDeMembroForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'] = "Não valido!"
    else: 
        context['form'] = novaCategoriaDeMembroForm()
    return render(request, "novaCategoriaDeMembro.html", context)