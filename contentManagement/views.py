from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms.novoItemCarousel import novoItemCarouselForm
from .forms.novoOuEditarProjeto import novoOuEditarProjetoForm
from .forms.novoOuEditarPostRevista import novoOuEditarPostRevistaForm
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
    context = {"titulo": "Novo Item do Carrousel", 
               "observacoes": ["Imagem: coloque o link da imagem que aparecerá no carousel, a imagem devera ser 1600x900", 
                               "Url: link de onde o usuario irá quando clicar na imagem"],}
    if request.method == "POST":
        context['form'] = novoItemCarouselForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novoItemCarouselForm()
    return render(request, "basicForm.html", context)


@login_required
def novoProjeto(request):
    context = {"titulo": "Novo Projeto", "observacoes": ["Capa: Coloque o link da imagem que será a capa"]}
    if request.method == "POST":
        context['form'] = novoOuEditarProjetoForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarProjetoForm()
    return render(request, "basicForm.html", context)


@login_required
def editarProjeto(request):
    context = {}
    items = Projeto.objects.all().order_by("-dataHora")
    context["items"] = items
    return render(request, "editarProjeto.html", context)


@login_required
def editarProjetoId(request, id):
    context = {"titulo": "Editando Projeto", "observacoes": ["Capa: Coloque o link da imagem que será a capa"]}
    instance = Projeto.objects.filter(id=id)[0]
    if request.method == "POST":
        context['form'] = novoOuEditarProjetoForm(request.POST, instance=instance)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarProjetoForm(instance=instance)
    return render(request, "basicForm.html", context)


@login_required
def novoPostRevista(request):
    context = {"titulo": "Novo Post De Revista", "observacoes": ["Capa: Coloque o link da imagem que será a capa"]}
    if request.method == "POST":
        context['form'] = novoOuEditarPostRevistaForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarPostRevistaForm()
    return render(request, "basicForm.html", context)


@login_required
def novaEdicaoDeRevista(request):
    context = {"titulo": "Nova Edição", "observacoes": [""]}
    if request.method == "POST":
        context['form'] = novaEdicaoDeRevistaForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novaEdicaoDeRevistaForm()
        context['erro'] = ""
    return render(request, "basicForm.html", context)


@login_required
def editarPostRevista(request):
    context = {}
    items = Revista.objects.all().order_by("-edicao", "-dataHora")
    context["items"] = items
    return render(request, "editarPostRevista.html", context)


@login_required
def editarPostRevistaId(request, id):
    context = {"titulo": "Editando Post De Revista", "observacoes": ["Capa: Coloque o link da imagem que será a capa"]}
    instance=Revista.objects.filter(id=id)[0]
    if request.method == "POST":
        context['form'] = novoOuEditarPostRevistaForm(request.POST, instance=instance)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarPostRevistaForm(instance=instance)
    return render(request, "basicForm.html", context)


@login_required
def novoMembro(request):
    context = {"titulo": "Novo Membro", "observacoes": [""]}
    if request.method == "POST":
        context['form'] = novoMembroForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novoMembroForm()
    return render(request, "basicForm.html", context)


@login_required
def novaCategoriaDeMembro(request):
    context = {"titulo": "Nova Categoria de Memebro", "observacoes": [""]}
    if request.method == "POST":
        context['form'] = novaCategoriaDeMembroForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'].errors
    else: 
        context['form'] = novaCategoriaDeMembroForm()
    return render(request, "basicForm.html", context)