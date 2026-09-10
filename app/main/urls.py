from django.urls import path
from . import views


urlpatterns = [
    path("", views.home.as_view(), name="home"),
    path("busca/", views.busca.as_view(), name="busca"),
    path("institucional/", views.institucional.as_view(), name="institucional"),
    path("sobre/", views.sobre.as_view(), name="sobre"),
    path("parceiros/", views.parceiros.as_view(), name="parceiros"),
    path("mapa/", views.mapa.as_view(), name="mapa"),
    path("acessibilidade/", views.acessibilidade.as_view(), name="acessibilidade"),
    path("expediente/", views.expediente.as_view(), name="expediente"),
    path("contato/", views.contato.as_view(), name="contato"),
]
