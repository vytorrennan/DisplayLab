from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.utils.text import slugify
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


def rangePages(quantasPaginasMostrar, page_obj):
    if (page_obj.number <= page_obj.paginator.num_pages - (quantasPaginasMostrar + 1)):
        if (page_obj.number == 1):
            rangePages = range(page_obj.number, page_obj.number + (quantasPaginasMostrar + 1))
        else:
            rangePages = range(page_obj.number - 1, page_obj.number + (quantasPaginasMostrar + 1))
    else:
        if (page_obj.number == 1):
            rangePages = range(page_obj.number, page_obj.paginator.num_pages + 1)
        else:
            rangePages = range(page_obj.number - 1, page_obj.paginator.num_pages + 1)
    return rangePages


# Create your views here.
@method_decorator(login_required, name="dispatch")
class contentManagement(View):
    def get(self, request):
        return render(request, "contentManagement.html")


@method_decorator(login_required, name="dispatch")
class novoItemCarousel(View):
    context = {"titulo": "Novo Item do Carrousel",
               "observacoes": ["Imagem: coloque o link da imagem que aparecerá no carousel, a imagem devera ser 1600x900", 
                               "Url: link de onde o usuario irá quando clicar na imagem"], 
                "linkColecao": "membroCarouselColecoes"}
    
    def get(self, request):
        self.context['form'] = novoOuEditarItemCarouselForm()
        return render(request, "basicFormWithImages.html", self.context)
    
    def post(self, request):
        self.context['form'] = novoOuEditarItemCarouselForm(request.POST)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Novo item de carousel cadastrado com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicFormWithImages.html", self.context)


@method_decorator(login_required, name="dispatch")
class editarItemCarousel(View):
    context = {}
    def get(self, request):
        items = carouselItem.objects.order_by("-id")
        paginator = Paginator(items, 30)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        quantasPaginasMostrar = 9
        self.context["rangePages"] = rangePages(quantasPaginasMostrar, page_obj)
        self.context["page_obj"] = page_obj
        return render(request, "editarItemCarousel.html", self.context)


@method_decorator(login_required, name="dispatch")
class editarItemCarouselId(View):
    context = {"titulo": "Editando Item De Carousel",
                "observacoes": ["Imagem: coloque o link da imagem que aparecerá no carousel, a imagem devera ser 1600x900", 
                                "Url: link de onde o usuario irá quando clicar na imagem"]}

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(carouselItem, id=kwargs['id'])
        self.context['form'] = novoOuEditarItemCarouselForm(instance=instance)
        return render(request, "basicForm.html", self.context)
    
    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(carouselItem, id=kwargs['id'])
        self.context['form'] = novoOuEditarItemCarouselForm(request.POST, instance=instance)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Item de carousel editado com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class membroCarouselColecoes(View):
    context = {"urlNovaColecao": "membroCarouselNovaColecao",
                "urlAdicionarImagem": "membroCarouselAdicionarImagem",
                "urllinksImagens": "linksImagensMembroCarousel"}
    
    def get(self, request):
        Colecoes = membroCarouselColecaoDeImagem.objects.order_by("-id")
        paginator = Paginator(Colecoes, 30)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        quantasPaginasMostrar = 9
        self.context["page_obj"] = page_obj
        self.context["rangePages"] = rangePages(quantasPaginasMostrar, page_obj)
        return render(request, "colecoesDeImagens.html", self.context)


@method_decorator(login_required, name="dispatch")
class membroCarouselNovaColecao(View):
    context = {"titulo": "Nova coleção de imagens", 
               "observacoes": ["Digite o nome da coleção (Nome do membro ou projeto)", "Use somente letras e/ou numeros, sem espaços"]}
    
    def get(self, request):
        self.context['form'] = membroCarouselNovaColecaoDeImagensForm()
        return render(request, "basicForm.html", self.context)

    def post(self, request):
        self.context['form'] = membroCarouselNovaColecaoDeImagensForm(request.POST)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Nova coleção cadastrada com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class membroCarouselAdicionarImagem(View):
    context = {"titulo": "Nova imagem"}

    def get(self, request):
        self.context['form'] = membroCarouselNovaImagemForm()
        return render(request, "basicForm.html", self.context)
    
    def post(self, request):
        fileName = request.FILES['imagem'].name
        fileExtensionPosition = fileName.rfind(".")
        fileExtension = fileName[fileExtensionPosition:]
        request.FILES['imagem'].name = slugify(fileName[:fileExtensionPosition]) + fileExtension
        self.context['form'] = membroCarouselNovaImagemForm(request.POST, request.FILES)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Nova imagem adicionada com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class linksImagensMembroCarousel(View):
    def get(self, request, *args, **kwargs):
        context = {"titulo": "Coleção: " + kwargs['colecao'],
                   "parteParaRemoverDaUrl": "main/static/"}
        context['Imagens'] = membroCarouselImagem.objects.filter(colecao=kwargs['colecao']).order_by("-id")
        return render(request, "linksDeImagens.html", context)


@method_decorator(login_required, name="dispatch")
class novoProjeto(View):
    context = {"titulo": "Novo Projeto",
               "observacoes": ["Capa: Coloque o link da imagem que será a capa"],
               "linkColecao": "projetoColecoes"}

    def get(self, request):
        self.context['form'] = novoOuEditarProjetoForm()
        return render(request, "basicFormWithImages.html", self.context)
    
    def post(self, request):
        self.context['form'] = novoOuEditarProjetoForm(request.POST)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Novo projeto cadastrado com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicFormWithImages.html", self.context)


@method_decorator(login_required, name="dispatch")
class editarProjeto(View):
    context = {}

    def get(self, request):
        Projetos = Projeto.objects.all().order_by("-dataHora")
        paginator = Paginator(Projetos, 30)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        quantasPaginasMostrar = 9
        self.context["rangePages"] = rangePages(quantasPaginasMostrar, page_obj)
        self.context["page_obj"] = page_obj
        return render(request, "editarProjeto.html", self.context)


@method_decorator(login_required, name="dispatch")
class editarProjetoId(View):
    context = {"titulo": "Editando Projeto", "observacoes": ["Capa: Coloque o link da imagem que será a capa"]}

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(Projeto, id=kwargs['id'])
        self.context['form'] = novoOuEditarProjetoForm(instance=instance)
        return render(request, "basicForm.html", self.context)
    
    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Projeto, id=kwargs['id'])
        self.context['form'] = novoOuEditarProjetoForm(request.POST, instance=instance)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Projeto editado com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class projetoColecoes(View):
    context = {"urlNovaColecao": "projetoNovaColecao",
               "urlAdicionarImagem": "projetoAdicionarImagem",
               "urllinksImagens": "linksImagensProjeto"}
    
    def get(self, request):
        Colecoes = projetoColecaoDeImagem.objects.order_by("-id")
        paginator = Paginator(Colecoes, 30)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        quantasPaginasMostrar = 9
        self.context["page_obj"] = page_obj
        self.context["rangePages"] = rangePages(quantasPaginasMostrar, page_obj)
        return render(request, "colecoesDeImagens.html", self.context)


@method_decorator(login_required, name="dispatch")
class projetoNovaColecao(View):
    context = {"titulo": "Nova coleção de imagens", 
               "observacoes": ["Digite o nome da coleção (Nome do projeto)", "Use somente letras e/ou numeros, sem espaços"]}
    
    def get(self, request):
        self.context['form'] = projetoNovaColecaoDeImagensForm()
        return render(request, "basicForm.html", self.context)

    def post(self, request):
        self.context['form'] = projetoNovaColecaoDeImagensForm(request.POST)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Nova coleção cadastrada com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class projetoAdicionarImagem(View):
    context = {"titulo": "Nova imagem"}

    def get(self, request):
        self.context['form'] = projetoNovaImagemForm()
        return render(request, "basicForm.html", self.context)
    
    def post(self, request):
        fileName = request.FILES['imagem'].name
        fileExtensionPosition = fileName.rfind(".")
        fileExtension = fileName[fileExtensionPosition:]
        request.FILES['imagem'].name = slugify(fileName[:fileExtensionPosition]) + fileExtension
        self.context['form'] = projetoNovaImagemForm(request.POST, request.FILES)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Nova imagem adicionada com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class linksImagensProjeto(View):
    def get(self, request, *args, **kwargs):
        context = {"titulo": "Coleção: " + kwargs['colecao'],
                   "parteParaRemoverDaUrl": "projetos/static/"}
        context['Imagens'] = projetoImagem.objects.filter(colecao=kwargs['colecao']).order_by("-id")
        return render(request, "linksDeImagens.html", context)


@method_decorator(login_required, name="dispatch")
class novoPostRevista(View):
    context = {"titulo": "Novo Post De Revista", 
               "observacoes": ["Capa: Coloque o link da imagem que será a capa"],
               "linkColecao": "revistaColecoes"}

    def get(self, request):
        self.context['form'] = novoOuEditarPostRevistaForm()
        return render(request, "basicFormWithImages.html", self.context)
    
    def post(self, request):
        self.context['form'] = novoOuEditarPostRevistaForm(request.POST)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Novo post de revista cadastrado com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicFormWithImages.html", self.context)


@method_decorator(login_required, name="dispatch")
class editarPostRevista(View):
    context = {}

    def get(self, request):
        Posts = Revista.objects.all().order_by("-edicao", "-dataHora")
        paginator = Paginator(Posts, 30)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        quantasPaginasMostrar = 9
        self.context["rangePages"] = rangePages(quantasPaginasMostrar, page_obj)
        self.context["page_obj"] = page_obj
        return render(request, "editarPostRevista.html", self.context)


@method_decorator(login_required, name="dispatch")
class editarPostRevistaId(View):
    context = {"titulo": "Editando Post De Revista", "observacoes": ["Capa: Coloque o link da imagem que será a capa"]}

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(Revista, id=kwargs['id'])
        self.context['form'] = novoOuEditarPostRevistaForm(instance=instance)
        return render(request, "basicForm.html", self.context)
    
    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Revista, id=kwargs['id'])
        self.context['form'] = novoOuEditarPostRevistaForm(request.POST, instance=instance)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Post de revista editado com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class novaEdicaoDeRevista(View):
    context = {"titulo": "Nova Edição", "observacoes": [""]}

    def get(self, request):
        self.context['form'] = novoOuEditarEdicaoDeRevistaForm()
        return render(request, "basicForm.html", self.context)
    
    def post(self, request):
        self.context['form'] = novoOuEditarEdicaoDeRevistaForm(request.POST)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Nova edição de revista cadastrada com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class editarEdicaoDeRevista(View):
    context = {}

    def get(self, request):
        Edicoes = edicao.objects.order_by("-edicao")
        paginator = Paginator(Edicoes, 30)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        quantasPaginasMostrar = 9
        self.context["rangePages"] = rangePages(quantasPaginasMostrar, page_obj)
        self.context["page_obj"] = page_obj
        return render(request, "editarEdicaoDeRevista.html", self.context)


@method_decorator(login_required, name="dispatch")
class editarEdicaoDeRevistaId(View):
    context = {"titulo": "Editando Edição De Revista", "observacoes": [""]}

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(edicao, id=kwargs['id'])
        self.context['form'] = novoOuEditarEdicaoDeRevistaForm(instance=instance)
        return render(request, "basicForm.html", self.context)
    
    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(edicao, id=kwargs['id'])
        self.context['form'] = novoOuEditarEdicaoDeRevistaForm(request.POST, instance=instance)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Edição editada com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class revistaColecoes(View):
    context = {"urlNovaColecao": "revistaNovaColecao",
               "urlAdicionarImagem": "revistaAdicionarImagem",
               "urllinksImagens": "linksImagensRevista"}
    
    def get(self, request):
        Colecoes = revistaColecaoDeImagem.objects.order_by("-id")
        paginator = Paginator(Colecoes, 30)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        quantasPaginasMostrar = 9
        self.context["page_obj"] = page_obj
        self.context["rangePages"] = rangePages(quantasPaginasMostrar, page_obj)
        return render(request, "colecoesDeImagens.html", self.context)


@method_decorator(login_required, name="dispatch")
class revistaNovaColecao(View):
    context = {"titulo": "Nova coleção de imagens", 
               "observacoes": ["Digite o nome da coleção (Nome do post de revista)", "Use somente letras e/ou numeros, sem espaços"]}
    
    def get(self, request):
        self.context['form'] = revistaNovaColecaoDeImagensForm()
        return render(request, "basicForm.html", self.context)

    def post(self, request):
        self.context['form'] = revistaNovaColecaoDeImagensForm(request.POST)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Nova coleção cadastrada com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class revistaAdicionarImagem(View):
    context = {"titulo": "Nova imagem"}

    def get(self, request):
        self.context['form'] = revistaNovaImagemForm()
        return render(request, "basicForm.html", self.context)
    
    def post(self, request):
        fileName = request.FILES['imagem'].name
        fileExtensionPosition = fileName.rfind(".")
        fileExtension = fileName[fileExtensionPosition:]
        request.FILES['imagem'].name = slugify(fileName[:fileExtensionPosition]) + fileExtension
        self.context['form'] = revistaNovaImagemForm(request.POST, request.FILES)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Nova imagem adicionada com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class linksImagensRevista(View):
    def get(self, request, *args, **kwargs):
        context = {"titulo": "Coleção: " + kwargs['colecao'],
                   "parteParaRemoverDaUrl": "revista/static/"}
        context['Imagens'] = revistaImagem.objects.filter(colecao=kwargs['colecao']).order_by("-id")
        return render(request, "linksDeImagens.html", context)


@method_decorator(login_required, name="dispatch")
class novoMembro(View):
    context = {"titulo": "Novo Membro", 
               "observacoes": [""],
               "linkColecao": "membroCarouselColecoes"}
    
    def get(self, request):
        self.context['form'] = novoOuEditarMembroForm()
        return render(request, "basicFormWithImages.html", self.context)
    
    def post(self, request):
        self.context['form'] = novoOuEditarMembroForm(request.POST)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Novo membro cadastrado com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicFormWithImages.html", self.context)


@method_decorator(login_required, name="dispatch")
class editarMembro(View):
    context = {}

    def get(self, request):
        Membros = Membro.objects.order_by("-categoria")
        paginator = Paginator(Membros, 30)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        quantasPaginasMostrar = 9
        self.context["rangePages"] = rangePages(quantasPaginasMostrar, page_obj)
        self.context["page_obj"] = page_obj
        return render(request, "editarMembro.html", self.context)


@method_decorator(login_required, name="dispatch")
class editarMembroId(View):
    context = {"titulo": "Editando membro", "observacoes": [""]}

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(Membro, id=kwargs['id'])
        self.context['form'] = novoOuEditarMembroForm(instance=instance)
        return render(request, "basicForm.html", self.context)
    
    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Membro, id=kwargs['id'])
        self.context['form'] = novoOuEditarMembroForm(request.POST, instance=instance)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Membro editado com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class novaCategoriaDeMembro(View):
    context = {"titulo": "Nova Categoria de Membro", "observacoes": [""]}

    def get(self, request):
        self.context['form'] = novoOuEditarCategoriaDeMembroForm()
        return render(request, "basicForm.html", self.context)
    def post(self, request):
        self.context['form'] = novoOuEditarCategoriaDeMembroForm(request.POST)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Nova categoria de membro cadastrado com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class editarCategoriaDeMembro(View):
    context = {}

    def get(self, request):
        Categorias = membroCategoria.objects.order_by("-categoria")
        paginator = Paginator(Categorias, 30)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        quantasPaginasMostrar = 9
        self.context["rangePages"] = rangePages(quantasPaginasMostrar, page_obj)
        self.context["page_obj"] = page_obj
        return render(request, "editarCategoriaDeMembro.html", self.context)



@method_decorator(login_required, name="dispatch")
class editarCategoriaDeMembroId(View):
    context = {"titulo": "Editando Categoria", "observacoes": [""]}

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(membroCategoria, id=kwargs['id'])
        self.context['form'] = novoOuEditarCategoriaDeMembroForm(instance=instance)
        return render(request, "basicForm.html", self.context)
    
    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(membroCategoria, id=kwargs['id'])
        self.context['form'] = novoOuEditarCategoriaDeMembroForm(request.POST, instance=instance)
        if self.context['form'].is_valid():
            self.context['form'].save()
            messages.success(request, "Categoria de membro editado com sucesso!")
        else:
            self.context['form'].errors
        return render(request, "basicForm.html", self.context)
