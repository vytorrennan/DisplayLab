from django.urls import path
from . import views

urlpatterns = [
    path("", views.contentManagement, name="contentManagement"),
    path("novoItemCarousel/", views.novoItemCarousel, name="novoItemCarousel"),
    path("novoProjeto/", views.novoProjeto, name="novoProjeto"),
]