from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.utils.text import slugify
from ..forms.projetos.novoOuEditarProjeto import novoOuEditarProjetoForm
from ..forms.projetos.projetoNovaColecaoDeImagens import projetoNovaColecaoDeImagensForm
from ..forms.projetos.projetoNovaImagem import projetoNovaImagemForm
from projetos.models import projetoColecaoDeImagem
from projetos.models import projetoImagem
from projetos.models import Projeto
from .viewsHome import rangePages


@method_decorator(login_required, name="dispatch")
class novoProjeto(View):
    context = {
        "titulo": "Novo Projeto",
        "observacoes": ["Capa: Coloque o link da imagem que será a capa"],
        "linkColecao": "projetoColecoes",
    }

    def get(self, request):
        self.context["form"] = novoOuEditarProjetoForm()
        return render(request, "basicFormWithImages.html", self.context)

    def post(self, request):
        self.context["form"] = novoOuEditarProjetoForm(request.POST)
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Novo projeto cadastrado com sucesso!")
        else:
            self.context["form"].errors
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
    context = {
        "titulo": "Editando Projeto",
        "observacoes": ["Capa: Coloque o link da imagem que será a capa"],
    }

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(Projeto, id=kwargs["id"])
        self.context["form"] = novoOuEditarProjetoForm(instance=instance)
        return render(request, "basicForm.html", self.context)

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Projeto, id=kwargs["id"])
        self.context["form"] = novoOuEditarProjetoForm(request.POST, instance=instance)
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Projeto editado com sucesso!")
        else:
            self.context["form"].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class projetoColecoes(View):
    context = {
        "urlNovaColecao": "projetoNovaColecao",
        "urlAdicionarImagem": "projetoAdicionarImagem",
        "urllinksImagens": "linksImagensProjeto",
    }

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
    context = {
        "titulo": "Nova coleção de imagens",
        "observacoes": [
            "Digite o nome da coleção (Nome do projeto)",
            "Use somente letras e/ou numeros, sem espaços",
        ],
    }

    def get(self, request):
        self.context["form"] = projetoNovaColecaoDeImagensForm()
        return render(request, "basicForm.html", self.context)

    def post(self, request):
        self.context["form"] = projetoNovaColecaoDeImagensForm(request.POST)
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Nova coleção cadastrada com sucesso!")
        else:
            self.context["form"].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class projetoAdicionarImagem(View):
    context = {"titulo": "Nova imagem"}

    def get(self, request):
        self.context["form"] = projetoNovaImagemForm()
        return render(request, "basicForm.html", self.context)

    def post(self, request):
        fileName = request.FILES["imagem"].name
        fileExtensionPosition = fileName.rfind(".")
        fileExtension = fileName[fileExtensionPosition:]
        request.FILES["imagem"].name = (
            slugify(fileName[:fileExtensionPosition]) + fileExtension
        )
        self.context["form"] = projetoNovaImagemForm(request.POST, request.FILES)
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Nova imagem adicionada com sucesso!")
        else:
            self.context["form"].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class linksImagensProjeto(View):
    def get(self, request, *args, **kwargs):
        context = {
            "titulo": "Coleção: " + kwargs["colecao"],
            "parteParaRemoverDaUrl": "projetos/",
        }
        context["Imagens"] = projetoImagem.objects.filter(
            colecao=kwargs["colecao"]
        ).order_by("-id")
        return render(request, "linksDeImagens.html", context)
