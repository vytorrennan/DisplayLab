from django.shortcuts import render

# Create your views here.
def novoProjeto(request):
    return render(request, "novoProjeto.html")