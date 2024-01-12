from django.urls import path
from . import views

urlpatterns = [
    path("", views.contentManagement, name="contentManagement"),
    path("novoItemCarousel/", views.novoItemCarousel, name="novoItemCarousel"),
    path("novoProjeto/", views.novoProjeto, name="novoProjeto"),
    path("novoPostRevista/", views.novoPostRevista, name="novoPostRevista"),
    path("novaEdicaoDeRevista/", views.novaEdicaoDeRevista, name="novaEdicaoDeRevista"),
    path("editarPostRevista/", views.editarPostRevista, name="editarPostRevista"),
    path("editarPostRevista/<int:id>", views.editarPostRevista, name="editarPostRevista"),
    path("novoMembro/", views.novoMembro, name="novoMembro"),
    path("novaCategoriaDeMembro/", views.novaCategoriaDeMembro, name="novaCategoriaDeMembro"),
]