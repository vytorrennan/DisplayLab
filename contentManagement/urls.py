from django.urls import path
from . import views

urlpatterns = [
    path("", views.contentManagement, name="contentManagement"),

    path("revistaColecoes/", views.revistaColecoes, name="revistaColecoes"),
    path("revistaColecoes/novaColecao", views.revistaNovaColecao, name="revistaNovaColecao"),
    path("revistaColecoes/projetoAdicionarImagem", views.revistaAdicionarImagem, name="revistaAdicionarImagem"),
    path("revistaColecoes/linksImagensProjeto/<str:colecao>", views.linksImagensRevista, name="linksImagensRevista"),

    path("novoItemCarousel/", views.novoItemCarousel, name="novoItemCarousel"),
    path("editarItemCarousel/", views.editarItemCarousel, name="editarItemCarousel"),
    path("editarItemCarousel/<int:id>", views.editarItemCarouselId, name="editarItemCarouselId"),

    path("novoProjeto/", views.novoProjeto, name="novoProjeto"),
    path("editarProjeto/", views.editarProjeto, name="editarProjeto"),
    path("editarProjeto/<int:id>", views.editarProjetoId, name="editarProjetoId"),
    path("projetoColecoes/", views.projetoColecoes, name="projetoColecoes"),
    path("projetoColecoes/novaColecao", views.projetoNovaColecao, name="projetoNovaColecao"),
    path("projetoColecoes/projetoAdicionarImagem", views.projetoAdicionarImagem, name="projetoAdicionarImagem"),
    path("projetoColecoes/linksImagensProjeto/<str:colecao>", views.linksImagensProjeto, name="linksImagensProjeto"),

    path("novoPostRevista/", views.novoPostRevista, name="novoPostRevista"),
    path("novaEdicaoDeRevista/", views.novaEdicaoDeRevista, name="novaEdicaoDeRevista"),
    path("editarPostRevista/", views.editarPostRevista, name="editarPostRevista"),
    path("editarPostRevista/<int:id>", views.editarPostRevistaId, name="editarPostRevistaId"),
    path("editarEdicaoDeRevista/", views.editarEdicaoDeRevista, name="editarEdicaoDeRevista"),
    path("editarEdicaoDeRevista/<int:id>", views.editarEdicaoDeRevistaId, name="editarEdicaoDeRevistaId"),

    path("novoMembro/", views.novoMembro, name="novoMembro"),
    path("editarMembro/", views.editarMembro, name="editarMembro"),
    path("editarMembro/<int:id>", views.editarMembroId, name="editarMembroId"),
    path("novaCategoriaDeMembro/", views.novaCategoriaDeMembro, name="novaCategoriaDeMembro"),
    path("editarCategoriaDeMembro/", views.editarCategoriaDeMembro, name="editarCategoriaDeMembro"),
    path("editarCategoriaDeMembro/<int:id>", views.editarCategoriaDeMembroId, name="editarCategoriaDeMembroId"),
]