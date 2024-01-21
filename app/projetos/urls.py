from django.urls import path
from . import views


urlpatterns = [
    path("projetos/", views.projetos.as_view(), name="projetos"),
    path("projetos/<slug:url>/", views.paginaDeProjeto.as_view(), name="paginaDeProjeto"),
]
