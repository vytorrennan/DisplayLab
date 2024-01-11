from django.shortcuts import render
from .models import Revista

# Create your views here.


def revista(request):
    posts = Revista.objects.all()
    context = {"posts": posts}
    return render(request, "revista.html", context)


def paginaDePost(request, url):
    post = Revista.objects.filter(url=url)
    context = {"post": post[0]}
    return render(request, "paginaDePost.html", context)