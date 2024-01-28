from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.utils.text import slugify
from ..forms.revista.novoOuEditarPostRevista import novoOuEditarPostRevistaForm
from ..forms.revista.novoOuEditarEdicaoDeRevista import novoOuEditarEdicaoDeRevistaForm
from ..forms.revista.revistaNovaColecaoDeImagens import revistaNovaColecaoDeImagensForm
from ..forms.revista.revistaNovaImagem import revistaNovaImagemForm
from revista.models import Revista
from revista.models import revistaColecaoDeImagem
from revista.models import revistaImagem
from revista.models import edicao
from .viewsHome import rangePages


@method_decorator(login_required, name="dispatch")
class novoPostRevista(View):
    context = {
        "titulo": "Novo Post De Revista",
        "observacoes": ["Capa: Coloque o link da imagem que será a capa"],
        "linkColecao": "revistaColecoes",
    }

    def get(self, request):
        self.context["form"] = novoOuEditarPostRevistaForm()
        return render(request, "basicFormWithImages.html", self.context)

    def post(self, request):
        self.context["form"] = novoOuEditarPostRevistaForm(request.POST)
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Novo post de revista cadastrado com sucesso!")
        else:
            self.context["form"].errors
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
    context = {
        "titulo": "Editando Post De Revista",
        "observacoes": ["Capa: Coloque o link da imagem que será a capa"],
    }

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(Revista, id=kwargs["id"])
        self.context["form"] = novoOuEditarPostRevistaForm(instance=instance)
        return render(request, "basicForm.html", self.context)

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Revista, id=kwargs["id"])
        self.context["form"] = novoOuEditarPostRevistaForm(
            request.POST, instance=instance
        )
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Post de revista editado com sucesso!")
        else:
            self.context["form"].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class novaEdicaoDeRevista(View):
    context = {"titulo": "Nova Edição", "observacoes": [""]}

    def get(self, request):
        self.context["form"] = novoOuEditarEdicaoDeRevistaForm()
        return render(request, "basicForm.html", self.context)

    def post(self, request):
        self.context["form"] = novoOuEditarEdicaoDeRevistaForm(request.POST)
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Nova edição de revista cadastrada com sucesso!")
        else:
            self.context["form"].errors
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
        instance = get_object_or_404(edicao, id=kwargs["id"])
        self.context["form"] = novoOuEditarEdicaoDeRevistaForm(instance=instance)
        return render(request, "basicForm.html", self.context)

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(edicao, id=kwargs["id"])
        self.context["form"] = novoOuEditarEdicaoDeRevistaForm(
            request.POST, instance=instance
        )
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Edição editada com sucesso!")
        else:
            self.context["form"].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class revistaColecoes(View):
    context = {
        "urlNovaColecao": "revistaNovaColecao",
        "urlAdicionarImagem": "revistaAdicionarImagem",
        "urllinksImagens": "linksImagensRevista",
    }

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
    context = {
        "titulo": "Nova coleção de imagens",
        "observacoes": [
            "Digite o nome da coleção (Nome do post de revista)",
            "Use somente letras e/ou numeros, sem espaços",
        ],
    }

    def get(self, request):
        self.context["form"] = revistaNovaColecaoDeImagensForm()
        return render(request, "basicForm.html", self.context)

    def post(self, request):
        self.context["form"] = revistaNovaColecaoDeImagensForm(request.POST)
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Nova coleção cadastrada com sucesso!")
        else:
            self.context["form"].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class revistaAdicionarImagem(View):
    context = {"titulo": "Nova imagem"}

    def get(self, request):
        self.context["form"] = revistaNovaImagemForm()
        return render(request, "basicForm.html", self.context)

    def post(self, request):
        fileName = request.FILES["imagem"].name
        fileExtensionPosition = fileName.rfind(".")
        fileExtension = fileName[fileExtensionPosition:]
        request.FILES["imagem"].name = (
            slugify(fileName[:fileExtensionPosition]) + fileExtension
        )
        self.context["form"] = revistaNovaImagemForm(request.POST, request.FILES)
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Nova imagem adicionada com sucesso!")
        else:
            self.context["form"].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class linksImagensRevista(View):
    def get(self, request, *args, **kwargs):
        context = {
            "titulo": "Coleção: " + kwargs["colecao"],
            "parteParaRemoverDaUrl": "revista",
        }
        context["Imagens"] = revistaImagem.objects.filter(
            colecao=kwargs["colecao"]
        ).order_by("-id")
        return render(request, "linksDeImagens.html", context)
