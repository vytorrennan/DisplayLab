from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from . import models


def displaycast_list(request):
    displaycasts = models.DisplayCast.objects.order_by('-dataHora')
    
    # Paginação
    paginator = Paginator(displaycasts, 9)  # 9 itens por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Calcular range de páginas
    rangePages = range(1, paginator.num_pages + 1)
    
    context = {
        'page_obj': page_obj,
        'displaycasts': page_obj.object_list,
        'rangePages': rangePages,
    }
    
    return render(request, 'displaycast.html', context)


def displaycast_detail(request, url):
    displaycast = get_object_or_404(models.DisplayCast, url=url)
    context = {
        'displaycast': displaycast,
    }
    
    return render(request, 'paginaDeDisplayCast.html', context)
