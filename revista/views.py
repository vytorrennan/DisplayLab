from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Revista

# Create your views here.


def revista(request):
    posts = Revista.objects.filter(oculto=False).order_by("-edicao", "-dataHora")
    paginator = Paginator(posts, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    quantasPaginasMostrar = 9
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
    context = {"page_obj": page_obj, "rangePages": rangePages}
    return render(request, "revista.html", context)


def paginaDePost(request, url):
    post = Revista.objects.filter(url=url, oculto=False)
    context = {"post": post[0]}
    return render(request, "paginaDePost.html", context)