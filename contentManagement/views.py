from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms.novoProjeto import novoProjetoForm
from .forms.novoItemCarousel import novoItemCarouselForm

# Create your views here.
@login_required
def contentManagement(request):
    return render(request, "contentManagement.html")


@login_required
def novoProjeto(request):
    context = {}
    if request.method == "POST":
        context['form'] = novoProjetoForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'] = "Não valido!"
    else: 
        context['form'] = novoProjetoForm()
    return render(request, "novoProjeto.html", context)


@login_required
def novoItemCarousel(request):
    context = {}
    if request.method == "POST":
        context['form'] = novoItemCarouselForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
        else:
            context['form'] = "Não valido!"
    else: 
        context['form'] = novoItemCarouselForm()
    return render(request, "novoItemCarousel.html", context)