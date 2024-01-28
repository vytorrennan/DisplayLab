from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Projeto


class projetos(View):
    def get(self, request):
        projeto = Projeto.objects.filter(oculto=False).order_by("-dataHora")
        paginator = Paginator(projeto, 9)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        maxPages = 9
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
        context = {"page_obj": page_obj, "rangePages": rangePages}
        return render(request, "projetos.html", context)


class paginaDeProjeto(View):
    def get(self, request, *args, **kwargs):
        projeto = Projeto.objects.filter(url=kwargs["url"], oculto=False)
        context = {"projeto": projeto[0]}
        return render(request, "paginaDeProjeto.html", context)
