from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms.novoItemCarousel import novoItemCarouselForm
from .forms.novoProjeto import novoProjetoForm
from .forms.novoPostRevista import novoPostRevistaForm
from .forms.novoMembro import novoMembroForm
from .forms.novaCategoriaDeMembro import novaCategoriaDeMembroForm
from .forms.novaEdicaoDeRevista import novaEdicaoDeRevistaForm
from revista.models import Revista
from projetos.models import Projeto



# Create your views here.
@login_required
def contentManagement(request):
    return render(request, "contentManagement.html")


@login_required
def novoItemCarousel(request):
    context = {}
    if request.method == "POST":
        context['form'] = novoItemCarouselForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novoItemCarouselForm()
    return render(request, "novoItemCarousel.html", context)


@login_required
def novoProjeto(request):
    context = {}
    if request.method == "POST":
        context['form'] = novoProjetoForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novoProjetoForm()
    return render(request, "novoProjeto.html", context)


@login_required
def editarProjeto(request):
    context = {}
    items = Projeto.objects.all().order_by("-dataHora")
    context["items"] = items
    return render(request, "editarProjeto.html", context)


@login_required
def editarProjetoId(request, id):
    context = {}
    if request.method == "POST":
        context['form'] = novoProjetoForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novoProjetoForm(instance=Projeto.objects.filter(id=id)[0])
    return render(request, "novoProjeto.html", context)


@login_required
def novoPostRevista(request):
    context = {}
    if request.method == "POST":
        context['form'] = novoPostRevistaForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novoPostRevistaForm()
    return render(request, "novoPostRevista.html", context)


@login_required
def novaEdicaoDeRevista(request):
    context = {}
    if request.method == "POST":
        context['form'] = novaEdicaoDeRevistaForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novaEdicaoDeRevistaForm()
        context['erro'] = ""
    return render(request, "novaEdicaoDeRevista.html", context)


@login_required
def editarPostRevista(request):
    context = {}
    items = Revista.objects.all().order_by("-edicao", "-dataHora")
    context["items"] = items
    return render(request, "editarPostRevista.html", context)


@login_required
def editarPostRevistaId(request, id):
    context = {}
    if request.method == "POST":
        context['form'] = novoPostRevistaForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novoPostRevistaForm(instance=Revista.objects.filter(id=id)[0])
    return render(request, "novoPostRevista.html", context)


@login_required
def novoMembro(request):
    context = {}
    if request.method == "POST":
        context['form'] = novoMembroForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
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
            context['form'].errors
    else: 
        context['form'] = novaCategoriaDeMembroForm()
    return render(request, "novaCategoriaDeMembro.html", context)