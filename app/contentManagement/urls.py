from django.urls import path
from .views.viewsHome import *
from .views.viewsProjetos import *
from .views.viewsRevista import *
from .views.viewsSobre import *

urlpatterns = [
    path("", contentManagement.as_view(), name="contentManagement"),

    path("novoItemCarousel/", novoItemCarousel.as_view(), name="novoItemCarousel"),
    path("editarItemCarousel/", editarItemCarousel.as_view(), name="editarItemCarousel"),
    path("editarItemCarousel/<int:id>", editarItemCarouselId.as_view(), name="editarItemCarouselId"),
    path("membroCarouselColecoes/", membroCarouselColecoes.as_view(), name="membroCarouselColecoes"),
    path("membroCarouselColecoes/novaColecao", membroCarouselNovaColecao.as_view(), name="membroCarouselNovaColecao"),
    path("membroCarouselColecoes/AdicionarImagem", membroCarouselAdicionarImagem.as_view(), name="membroCarouselAdicionarImagem"),
    path("membroCarouselColecoes/linksImagens/<str:colecao>", linksImagensMembroCarousel.as_view(), name="linksImagensMembroCarousel"),

    path("novoProjeto/", novoProjeto.as_view(), name="novoProjeto"),
    path("editarProjeto/", editarProjeto.as_view(), name="editarProjeto"),
    path("editarProjeto/<int:id>", editarProjetoId.as_view(), name="editarProjetoId"),
    path("projetoColecoes/", projetoColecoes.as_view(), name="projetoColecoes"),
    path("projetoColecoes/novaColecao", projetoNovaColecao.as_view(), name="projetoNovaColecao"),
    path("projetoColecoes/AdicionarImagem", projetoAdicionarImagem.as_view(), name="projetoAdicionarImagem"),
    path("projetoColecoes/linksImagens/<str:colecao>", linksImagensProjeto.as_view(), name="linksImagensProjeto"),

    path("novoPostRevista/", novoPostRevista.as_view(), name="novoPostRevista"),
    path("editarPostRevista/", editarPostRevista.as_view(), name="editarPostRevista"),
    path("editarPostRevista/<int:id>", editarPostRevistaId.as_view(), name="editarPostRevistaId"),
    path("novaEdicaoDeRevista/", novaEdicaoDeRevista.as_view(), name="novaEdicaoDeRevista"),
    path("editarEdicaoDeRevista/", editarEdicaoDeRevista.as_view(), name="editarEdicaoDeRevista"),
    path("editarEdicaoDeRevista/<int:id>", editarEdicaoDeRevistaId.as_view(), name="editarEdicaoDeRevistaId"),
    path("revistaColecoes/", revistaColecoes.as_view(), name="revistaColecoes"),
    path("revistaColecoes/novaColecao", revistaNovaColecao.as_view(), name="revistaNovaColecao"),
    path("revistaColecoes/AdicionarImagem", revistaAdicionarImagem.as_view(), name="revistaAdicionarImagem"),
    path("revistaColecoes/linksImagens/<str:colecao>", linksImagensRevista.as_view(), name="linksImagensRevista"),

    path("novoMembro/", novoMembro.as_view(), name="novoMembro"),
    path("editarMembro/", editarMembro.as_view(), name="editarMembro"),
    path("editarMembro/<int:id>", editarMembroId.as_view(), name="editarMembroId"),
    path("novaCategoriaDeMembro/", novaCategoriaDeMembro.as_view(), name="novaCategoriaDeMembro"),
    path("editarCategoriaDeMembro/", editarCategoriaDeMembro.as_view(), name="editarCategoriaDeMembro"),
    path("editarCategoriaDeMembro/<int:id>", editarCategoriaDeMembroId.as_view(), name="editarCategoriaDeMembroId"),
]