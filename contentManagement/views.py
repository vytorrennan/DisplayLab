from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms.main.novoOuEditarItemCarousel import novoOuEditarItemCarouselForm
from .forms.projetos.novoOuEditarProjeto import novoOuEditarProjetoForm
from .forms.main.membroCarouselNovaColecaoDeImagens import membroCarouselNovaColecaoDeImagensForm
from .forms.main.membroCarouselNovaImagem import membroCarouselNovaImagemForm
from .forms.projetos.projetoNovaColecaoDeImagens import projetoNovaColecaoDeImagensForm
from .forms.projetos.projetoNovaImagem import projetoNovaImagemForm
from .forms.revista.novoOuEditarPostRevista import novoOuEditarPostRevistaForm
from .forms.revista.novoOuEditarEdicaoDeRevista import novoOuEditarEdicaoDeRevistaForm
from .forms.revista.revistaNovaColecaoDeImagens import revistaNovaColecaoDeImagensForm
from .forms.revista.revistaNovaImagem import revistaNovaImagemForm
from .forms.main.novoOuEditarMembro import novoOuEditarMembroForm
from .forms.main.novoOuEditarCategoriaDeMembro import novoOuEditarCategoriaDeMembroForm
from main.models import carouselItem
from main.models import membroCarouselColecaoDeImagem
from main.models import membroCarouselImagem
from projetos.models import projetoColecaoDeImagem
from projetos.models import projetoImagem
from projetos.models import Projeto
from revista.models import Revista
from revista.models import revistaColecaoDeImagem
from revista.models import revistaImagem
from revista.models import edicao
from main.models import Membro
from main.models import membroCategoria


# Create your views here.
@login_required
def contentManagement(request):
    return render(request, "contentManagement.html")


@login_required
def novoItemCarousel(request):
    context = {"titulo": "Novo Item do Carrousel", 
               "success": "",
               "observacoes": ["Imagem: coloque o link da imagem que aparecerá no carousel, a imagem devera ser 1600x900", 
                               "Url: link de onde o usuario irá quando clicar na imagem"]}
    if request.method == "POST":
        context['form'] = novoOuEditarItemCarouselForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Novo item de carousel cadastrado com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarItemCarouselForm()
    return render(request, "basicForm.html", context)


@login_required
def editarItemCarousel(request):
    context = {}
    items = carouselItem.objects.all()
    context["items"] = items
    return render(request, "editarItemCarousel.html", context)


@login_required
def editarItemCarouselId(request, id):
    context = {"titulo": "Editando Item De Carousel",
               "success": "", 
               "observacoes": ["Imagem: coloque o link da imagem que aparecerá no carousel, a imagem devera ser 1600x900", 
                               "Url: link de onde o usuario irá quando clicar na imagem"]}
    instance = carouselItem.objects.filter(id=id)[0]
    if request.method == "POST":
        context['form'] = novoOuEditarItemCarouselForm(request.POST, instance=instance)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Item de carousel editado com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarItemCarouselForm(instance=instance)
    return render(request, "basicForm.html", context)


@login_required
def membroCarouselColecoes(request):
    context = {"urlNovaColecao": "membroCarouselNovaColecao",
               "urlAdicionarImagem": "membroCarouselAdicionarImagem",
               "urllinksImagens": "linksImagensMembroCarousel"}
    Colecoes = membroCarouselColecaoDeImagem.objects.all()
    context["Colecoes"] = Colecoes
    return render(request, "colecoesDeImagens.html", context)


@login_required
def membroCarouselNovaColecao(request):
    context = {"titulo": "Nova coleção de imagens", 
               "success": "", 
               "observacoes": ["Digite o nome da coleção (Nome do membro ou projeto)"]}
    if request.method == "POST":
        context['form'] = membroCarouselNovaColecaoDeImagensForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Nova coleção cadastrada com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = membroCarouselNovaColecaoDeImagensForm()
    return render(request, "basicForm.html", context)


@login_required
def membroCarouselAdicionarImagem(request):
    context = {"titulo": "Nova imagem", 
                "success": ""}
    if request.method == "POST":
        request.FILES['imagem'].name = request.FILES['imagem'].name.replace(" ", "")
        context['form'] = membroCarouselNovaImagemForm(request.POST, request.FILES)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Nova imagem adicionada com sucesso!"
        else:
            context['form'].errors
    else:
        context['form'] = membroCarouselNovaImagemForm()
    return render(request, "basicForm.html", context)


@login_required
def linksImagensMembroCarousel(request, colecao):
    context = {"titulo": "Coleção: " + colecao,
               "parteParaRemoverDaUrl": "main/static/"}
    context['Imagens'] = membroCarouselImagem.objects.filter(colecao=colecao)
    return render(request, "linksDeImagens.html", context)


@login_required
def novoProjeto(request):
    context = {"titulo": "Novo Projeto", "success": "", "observacoes": ["Capa: Coloque o link da imagem que será a capa"]}
    if request.method == "POST":
        context['form'] = novoOuEditarProjetoForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Novo projeto cadastrado com sucesso!"
        else:
            context['form'].errors
    else:
        context['form'] = novoOuEditarProjetoForm()
    return render(request, "basicForm.html", context)


@login_required
def editarProjeto(request):
    context = {}
    Projetos = Projeto.objects.all().order_by("-dataHora")
    context["Projetos"] = Projetos
    return render(request, "editarProjeto.html", context)


@login_required
def editarProjetoId(request, id):
    context = {"titulo": "Editando Projeto", "success": "", "observacoes": ["Capa: Coloque o link da imagem que será a capa"]}
    instance = Projeto.objects.filter(id=id)[0]
    if request.method == "POST":
        context['form'] = novoOuEditarProjetoForm(request.POST, instance=instance)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Projeto editado com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarProjetoForm(instance=instance)
    return render(request, "basicForm.html", context)


@login_required
def projetoColecoes(request):
    context = {"urlNovaColecao": "projetoNovaColecao",
               "urlAdicionarImagem": "projetoAdicionarImagem",
               "urllinksImagens": "linksImagensProjeto"}
    Colecoes = projetoColecaoDeImagem.objects.all()
    context["Colecoes"] = Colecoes
    return render(request, "colecoesDeImagens.html", context)


@login_required
def projetoNovaColecao(request):
    context = {"titulo": "Nova coleção de imagens", 
               "success": "", 
               "observacoes": ["Digite o nome da coleção (Nome do projeto)"]}
    if request.method == "POST":
        context['form'] = projetoNovaColecaoDeImagensForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Nova coleção cadastrada com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = projetoNovaColecaoDeImagensForm()
    return render(request, "basicForm.html", context)


@login_required
def projetoAdicionarImagem(request):
    context = {"titulo": "Nova imagem", 
                "success": ""}
    if request.method == "POST":
        request.FILES['imagem'].name = request.FILES['imagem'].name.replace(" ", "")
        context['form'] = projetoNovaImagemForm(request.POST, request.FILES)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Nova imagem adicionada com sucesso!"
        else:
            context['form'].errors
    else:
        context['form'] = projetoNovaImagemForm()
    return render(request, "basicForm.html", context)


@login_required
def linksImagensProjeto(request, colecao):
    context = {"titulo": "Coleção: " + colecao,
               "parteParaRemoverDaUrl": "projetos/static/"}
    context['Imagens'] = projetoImagem.objects.filter(colecao=colecao)
    return render(request, "linksDeImagens.html", context)


@login_required
def novoPostRevista(request):
    context = {"titulo": "Novo Post De Revista", "success": "", "observacoes": ["Capa: Coloque o link da imagem que será a capa"]}
    if request.method == "POST":
        context['form'] = novoOuEditarPostRevistaForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Novo post de revista cadastrado com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarPostRevistaForm()
    return render(request, "basicForm.html", context)


@login_required
def editarPostRevista(request):
    context = {}
    Posts = Revista.objects.all().order_by("-edicao", "-dataHora")
    context["Posts"] = Posts
    return render(request, "editarPostRevista.html", context)


@login_required
def editarPostRevistaId(request, id):
    context = {"titulo": "Editando Post De Revista", "success": "", "observacoes": ["Capa: Coloque o link da imagem que será a capa"]}
    instance = Revista.objects.filter(id=id)[0]
    if request.method == "POST":
        context['form'] = novoOuEditarPostRevistaForm(request.POST, instance=instance)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Post de revista editado com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarPostRevistaForm(instance=instance)
    return render(request, "basicForm.html", context)


@login_required
def novaEdicaoDeRevista(request):
    context = {"titulo": "Nova Edição", "success": "", "observacoes": [""]}
    if request.method == "POST":
        context['form'] = novoOuEditarEdicaoDeRevistaForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Nova edição de revista cadastrada com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarEdicaoDeRevistaForm()
        context['erro'] = ""
    return render(request, "basicForm.html", context)


@login_required
def editarEdicaoDeRevista(request):
    context = {}
    Edicoes = edicao.objects.all().order_by("-edicao")
    context["Edicoes"] = Edicoes
    return render(request, "editarEdicaoDeRevista.html", context)


@login_required
def editarEdicaoDeRevistaId(request, id):
    context = {"titulo": "Editando Edição De Revista", "success": "", "observacoes": [""]}
    instance = edicao.objects.filter(id=id)[0]
    if request.method == "POST":
        context['form'] = novoOuEditarEdicaoDeRevistaForm(request.POST, instance=instance)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Edição editada com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarEdicaoDeRevistaForm(instance=instance)
    return render(request, "basicForm.html", context)


@login_required
def revistaColecoes(request):
    context = {"urlNovaColecao": "revistaNovaColecao",
               "urlAdicionarImagem": "revistaAdicionarImagem",
               "urllinksImagens": "linksImagensRevista"}
    Colecoes = revistaColecaoDeImagem.objects.all()
    context["Colecoes"] = Colecoes
    return render(request, "colecoesDeImagens.html", context)


@login_required
def revistaNovaColecao(request):
    context = {"titulo": "Nova coleção de imagens", 
               "success": "", 
               "observacoes": ["Digite o nome da coleção (Nome do post de revista)"]}
    if request.method == "POST":
        context['form'] = revistaNovaColecaoDeImagensForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Nova coleção cadastrada com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = revistaNovaColecaoDeImagensForm()
    return render(request, "basicForm.html", context)


@login_required
def revistaAdicionarImagem(request):
    context = {"titulo": "Nova imagem", 
                "success": ""}
    if request.method == "POST":
        request.FILES['imagem'].name = request.FILES['imagem'].name.replace(" ", "")
        context['form'] = revistaNovaImagemForm(request.POST, request.FILES)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Nova imagem adicionada com sucesso!"
        else:
            context['form'].errors
    else:
        context['form'] = revistaNovaImagemForm()
    return render(request, "basicForm.html", context)


@login_required
def linksImagensRevista(request, colecao):
    context = {"titulo": "Coleção: " + colecao,
               "parteParaRemoverDaUrl": "revista/static/"}
    context['Imagens'] = revistaImagem.objects.filter(colecao=colecao)
    return render(request, "linksDeImagens.html", context)


@login_required
def novoMembro(request):
    context = {"titulo": "Novo Membro", "success": "", "observacoes": [""]}
    if request.method == "POST":
        context['form'] = novoOuEditarMembroForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Novo membro cadastrado com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarMembroForm()
    return render(request, "basicForm.html", context)


@login_required
def editarMembro(request):
    context = {}
    Membros = Membro.objects.order_by("-categoria")
    context["Membros"] = Membros
    return render(request, "editarMembro.html", context)


@login_required
def editarMembroId(request, id):
    context = {"titulo": "Editando membro", "success": "", "observacoes": [""]}
    instance = Membro.objects.filter(id=id)[0]
    if request.method == "POST":
        context['form'] = novoOuEditarMembroForm(request.POST, instance=instance)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Membro editado com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarMembroForm(instance=instance)
    return render(request, "basicForm.html", context)


@login_required
def novaCategoriaDeMembro(request):
    context = {"titulo": "Nova Categoria de Membro", "success": "", "observacoes": [""]}
    if request.method == "POST":
        context['form'] = novoOuEditarCategoriaDeMembroForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Nova categoria de membro cadastrado com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarCategoriaDeMembroForm()
    return render(request, "basicForm.html", context)


@login_required
def editarCategoriaDeMembro(request):
    context = {}
    Categorias = membroCategoria.objects.order_by("-categoria")
    context["Categorias"] = Categorias
    return render(request, "editarCategoriaDeMembro.html", context)


@login_required
def editarCategoriaDeMembroId(request, id):
    context = {"titulo": "Editando Categoria", "success": "", "observacoes": [""]}
    instance = membroCategoria.objects.filter(id=id)[0]
    if request.method == "POST":
        context['form'] = novoOuEditarCategoriaDeMembroForm(request.POST, instance=instance)
        if context['form'].is_valid():
            context['form'].save()
            context['success'] = "Categoria de membro editado com sucesso!"
        else:
            context['form'].errors
    else: 
        context['form'] = novoOuEditarCategoriaDeMembroForm(instance=instance)
    return render(request, "basicForm.html", context)