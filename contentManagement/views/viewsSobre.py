from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.utils.text import slugify
from ..forms.sobre.novoOuEditarMembro import novoOuEditarMembroForm
from ..forms.sobre.novoOuEditarCategoriaDeMembro import novoOuEditarCategoriaDeMembroForm
from main.models import Membro
from main.models import membroCategoria
from .viewsHome import rangePages


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
