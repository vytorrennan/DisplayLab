from django.urls import path
from . import views

urlpatterns = [
    path("", views.contentManagement.as_view(), name="contentManagement"),

    path("novoItemCarousel/", views.novoItemCarousel.as_view(), name="novoItemCarousel"),
    path("editarItemCarousel/", views.editarItemCarousel.as_view(), name="editarItemCarousel"),
    path("editarItemCarousel/<int:id>", views.editarItemCarouselId.as_view(), name="editarItemCarouselId"),
    path("membroCarouselColecoes/", views.membroCarouselColecoes.as_view(), name="membroCarouselColecoes"),
    path("membroCarouselColecoes/novaColecao", views.membroCarouselNovaColecao.as_view(), name="membroCarouselNovaColecao"),
    path("membroCarouselColecoes/AdicionarImagem", views.membroCarouselAdicionarImagem.as_view(), name="membroCarouselAdicionarImagem"),
    path("membroCarouselColecoes/linksImagens/<str:colecao>", views.linksImagensMembroCarousel.as_view(), name="linksImagensMembroCarousel"),

    path("novoProjeto/", views.novoProjeto.as_view(), name="novoProjeto"),
    path("editarProjeto/", views.editarProjeto.as_view(), name="editarProjeto"),
    path("editarProjeto/<int:id>", views.editarProjetoId.as_view(), name="editarProjetoId"),
    path("projetoColecoes/", views.projetoColecoes.as_view(), name="projetoColecoes"),
    path("projetoColecoes/novaColecao", views.projetoNovaColecao.as_view(), name="projetoNovaColecao"),
    path("projetoColecoes/AdicionarImagem", views.projetoAdicionarImagem.as_view(), name="projetoAdicionarImagem"),
    path("projetoColecoes/linksImagens/<str:colecao>", views.linksImagensProjeto.as_view(), name="linksImagensProjeto"),

    path("novoPostRevista/", views.novoPostRevista, name="novoPostRevista"),
    path("novaEdicaoDeRevista/", views.novaEdicaoDeRevista, name="novaEdicaoDeRevista"),
    path("editarPostRevista/", views.editarPostRevista, name="editarPostRevista"),
    path("editarPostRevista/<int:id>", views.editarPostRevistaId, name="editarPostRevistaId"),
    path("editarEdicaoDeRevista/", views.editarEdicaoDeRevista, name="editarEdicaoDeRevista"),
    path("editarEdicaoDeRevista/<int:id>", views.editarEdicaoDeRevistaId, name="editarEdicaoDeRevistaId"),
    path("revistaColecoes/", views.revistaColecoes, name="revistaColecoes"),
    path("revistaColecoes/novaColecao", views.revistaNovaColecao, name="revistaNovaColecao"),
    path("revistaColecoes/AdicionarImagem", views.revistaAdicionarImagem, name="revistaAdicionarImagem"),
    path("revistaColecoes/linksImagens/<str:colecao>", views.linksImagensRevista, name="linksImagensRevista"),

    path("novoMembro/", views.novoMembro, name="novoMembro"),
    path("editarMembro/", views.editarMembro, name="editarMembro"),
    path("editarMembro/<int:id>", views.editarMembroId, name="editarMembroId"),
    path("novaCategoriaDeMembro/", views.novaCategoriaDeMembro, name="novaCategoriaDeMembro"),
    path("editarCategoriaDeMembro/", views.editarCategoriaDeMembro, name="editarCategoriaDeMembro"),
    path("editarCategoriaDeMembro/<int:id>", views.editarCategoriaDeMembroId, name="editarCategoriaDeMembroId"),
]