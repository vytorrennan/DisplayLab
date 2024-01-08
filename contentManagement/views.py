from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def contentManagement(request):
    return render(request, "contentManagement.html")


@login_required
def novoProjeto(request):
    return render(request, "novoProjeto.html")