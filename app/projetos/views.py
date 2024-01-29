from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Projeto
from contentManagement.views.viewsHome import rangePages


class projetos(View):
    def get(self, request):
        projeto = Projeto.objects.filter(oculto=False).order_by("-dataHora")
        paginator = Paginator(projeto, 9)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        rangePage = rangePages(9, page_obj)
        context = {"page_obj": page_obj, "rangePages": rangePage}
        return render(request, "projetos.html", context)


class paginaDeProjeto(View):
    def get(self, request, *args, **kwargs):
        projeto = Projeto.objects.filter(url=kwargs["url"], oculto=False)
        context = {"projeto": projeto[0]}
        return render(request, "paginaDeProjeto.html", context)
