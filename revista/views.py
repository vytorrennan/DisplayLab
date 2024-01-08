from django.shortcuts import render

# Create your views here.


def revista(request):
    return render(request, "revista.html")