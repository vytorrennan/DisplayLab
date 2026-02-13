from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Projeto
from revista.models import Revista
from contentManagement.views.viewsHome import rangePages


class projetos(View):
    def get(self, request):
        projeto = Projeto.objects.filter(oculto=False).order_by("-dataHora")
        itensPerPage = 9
        paginator = Paginator(projeto, itensPerPage)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        maxNumberOfPages = 9
        rangePage = rangePages(maxNumberOfPages, page_obj)

        ultimosPosts = Revista.objects.filter(oculto=False).order_by("-edicao", "-dataHora")[0:2]

        context = {"page_obj": page_obj, "rangePages": rangePage, "ultimosPosts": ultimosPosts}
        return render(request, "projetos.html", context)


class paginaDeProjeto(View):
    def get(self, request, *args, **kwargs):
        projeto = Projeto.objects.filter(url=kwargs["url"], oculto=False)
        context = {"projeto": projeto}
        return render(request, "paginaDeProjeto.html", context)
