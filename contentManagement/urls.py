from django.urls import path
from . import views

urlpatterns = [
    path("", views.contentManagement, name="contentManagement"),
    
    path("novoItemCarousel/", views.novoItemCarousel, name="novoItemCarousel"),

    path("novoProjeto/", views.novoProjeto, name="novoProjeto"),
    path("editarProjeto/", views.editarProjeto, name="editarProjeto"),
    path("editarProjeto/<int:id>", views.editarProjetoId, name="editarProjetoId"),

    path("novoPostRevista/", views.novoPostRevista, name="novoPostRevista"),
    path("novaEdicaoDeRevista/", views.novaEdicaoDeRevista, name="novaEdicaoDeRevista"),
    path("editarPostRevista/", views.editarPostRevista, name="editarPostRevista"),
    path("editarPostRevista/<int:id>", views.editarPostRevistaId, name="editarPostRevistaId"),

    path("novoMembro/", views.novoMembro, name="novoMembro"),
    path("editarMembro/", views.editarMembro, name="editarMembro"),
    path("editarMembro/<int:id>", views.editarMembroId, name="editarMembroId"),
    path("novaCategoriaDeMembro/", views.novaCategoriaDeMembro, name="novaCategoriaDeMembro"),
]