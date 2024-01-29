from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Revista
from contentManagement.views.viewsHome import rangePages

# Create your views here.


class revista(View):
    def get(self, request):
        posts = Revista.objects.filter(oculto=False).order_by("-edicao", "-dataHora")
        paginator = Paginator(posts, 12)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        rangePage = rangePages(12, page_obj)
        context = {"page_obj": page_obj, "rangePages": rangePage}
        return render(request, "revista.html", context)


class paginaDePost(View):
    def get(self, request, *args, **kwargs):
        post = Revista.objects.filter(url=kwargs["url"], oculto=False)
        context = {"post": post[0]}
        return render(request, "paginaDePost.html", context)
