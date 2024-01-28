from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.utils.text import slugify
from ..forms.home.novoOuEditarItemCarousel import novoOuEditarItemCarouselForm
from ..forms.home.membroCarouselNovaColecaoDeImagens import (
    membroCarouselNovaColecaoDeImagensForm,
)
from ..forms.home.membroCarouselNovaImagem import membroCarouselNovaImagemForm
from main.models import carouselItem
from main.models import membroCarouselColecaoDeImagem
from main.models import membroCarouselImagem


def rangePages(quantasPaginasMostrar, page_obj):
    maxPages = quantasPaginasMostrar
    currentPage = page_obj.number
    posteriorPage = currentPage - 1
    totalPages = page_obj.paginator.num_pages
    if currentPage <= totalPages - (maxPages + 1):
        if page_obj.number == 1:
            rangePages = range(currentPage, currentPage + (maxPages + 1))
        else:
            rangePages = range(posteriorPage, currentPage + (maxPages + 1))
    else:
        if page_obj.number == 1:
            rangePages = range(currentPage, totalPages + 1)
        else:
            rangePages = range(posteriorPage, totalPages + 1)
    return rangePages


@method_decorator(login_required, name="dispatch")
class contentManagement(View):
    def get(self, request):
        return render(request, "contentManagement.html")


@method_decorator(login_required, name="dispatch")
class novoItemCarousel(View):
    context = {
        "titulo": "Novo Item do Carrousel",
        "observacoes": [
            "Imagem: coloque o link da imagem que aparecerá no carousel, a imagem devera ser 1600x900",
            "Url: link de onde o usuario irá quando clicar na imagem",
        ],
        "linkColecao": "membroCarouselColecoes",
    }

    def get(self, request):
        self.context["form"] = novoOuEditarItemCarouselForm()
        return render(request, "basicFormWithImages.html", self.context)

    def post(self, request):
        self.context["form"] = novoOuEditarItemCarouselForm(request.POST)
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Novo item de carousel cadastrado com sucesso!")
        else:
            self.context["form"].errors
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
    context = {
        "titulo": "Editando Item De Carousel",
        "observacoes": [
            "Imagem: coloque o link da imagem que aparecerá no carousel, a imagem devera ser 1600x900",
            "Url: link de onde o usuario irá quando clicar na imagem",
        ],
    }

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(carouselItem, id=kwargs["id"])
        self.context["form"] = novoOuEditarItemCarouselForm(instance=instance)
        return render(request, "basicForm.html", self.context)

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(carouselItem, id=kwargs["id"])
        self.context["form"] = novoOuEditarItemCarouselForm(
            request.POST, instance=instance
        )
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Item de carousel editado com sucesso!")
        else:
            self.context["form"].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class membroCarouselColecoes(View):
    context = {
        "urlNovaColecao": "membroCarouselNovaColecao",
        "urlAdicionarImagem": "membroCarouselAdicionarImagem",
        "urllinksImagens": "linksImagensMembroCarousel",
    }

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
    context = {
        "titulo": "Nova coleção de imagens",
        "observacoes": [
            "Digite o nome da coleção (Nome do membro ou projeto)",
            "Use somente letras e/ou numeros, sem espaços",
        ],
    }

    def get(self, request):
        self.context["form"] = membroCarouselNovaColecaoDeImagensForm()
        return render(request, "basicForm.html", self.context)

    def post(self, request):
        self.context["form"] = membroCarouselNovaColecaoDeImagensForm(request.POST)
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Nova coleção cadastrada com sucesso!")
        else:
            self.context["form"].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class membroCarouselAdicionarImagem(View):
    context = {"titulo": "Nova imagem"}

    def get(self, request):
        self.context["form"] = membroCarouselNovaImagemForm()
        return render(request, "basicForm.html", self.context)

    def post(self, request):
        fileName = request.FILES["imagem"].name
        fileExtensionPosition = fileName.rfind(".")
        fileExtension = fileName[fileExtensionPosition:]
        request.FILES["imagem"].name = (
            slugify(fileName[:fileExtensionPosition]) + fileExtension
        )
        self.context["form"] = membroCarouselNovaImagemForm(request.POST, request.FILES)
        if self.context["form"].is_valid():
            self.context["form"].save()
            messages.success(request, "Nova imagem adicionada com sucesso!")
        else:
            self.context["form"].errors
        return render(request, "basicForm.html", self.context)


@method_decorator(login_required, name="dispatch")
class linksImagensMembroCarousel(View):
    def get(self, request, *args, **kwargs):
        context = {
            "titulo": "Coleção: " + kwargs["colecao"],
            "parteParaRemoverDaUrl": "main",
        }
        context["Imagens"] = membroCarouselImagem.objects.filter(
            colecao=kwargs["colecao"]
        ).order_by("-id")
        return render(request, "linksDeImagens.html", context)
