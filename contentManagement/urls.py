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

    path("novoPostRevista/", views.novoPostRevista.as_view(), name="novoPostRevista"),
    path("editarPostRevista/", views.editarPostRevista.as_view(), name="editarPostRevista"),
    path("editarPostRevista/<int:id>", views.editarPostRevistaId.as_view(), name="editarPostRevistaId"),
    path("novaEdicaoDeRevista/", views.novaEdicaoDeRevista.as_view(), name="novaEdicaoDeRevista"),
    path("editarEdicaoDeRevista/", views.editarEdicaoDeRevista.as_view(), name="editarEdicaoDeRevista"),
    path("editarEdicaoDeRevista/<int:id>", views.editarEdicaoDeRevistaId.as_view(), name="editarEdicaoDeRevistaId"),
    path("revistaColecoes/", views.revistaColecoes.as_view(), name="revistaColecoes"),
    path("revistaColecoes/novaColecao", views.revistaNovaColecao.as_view(), name="revistaNovaColecao"),
    path("revistaColecoes/AdicionarImagem", views.revistaAdicionarImagem.as_view(), name="revistaAdicionarImagem"),
    path("revistaColecoes/linksImagens/<str:colecao>", views.linksImagensRevista.as_view(), name="linksImagensRevista"),

    path("novoMembro/", views.novoMembro.as_view(), name="novoMembro"),
    path("editarMembro/", views.editarMembro.as_view(), name="editarMembro"),
    path("editarMembro/<int:id>", views.editarMembroId.as_view(), name="editarMembroId"),
    path("novaCategoriaDeMembro/", views.novaCategoriaDeMembro.as_view(), name="novaCategoriaDeMembro"),
    path("editarCategoriaDeMembro/", views.editarCategoriaDeMembro.as_view(), name="editarCategoriaDeMembro"),
    path("editarCategoriaDeMembro/<int:id>", views.editarCategoriaDeMembroId.as_view(), name="editarCategoriaDeMembroId"),
]