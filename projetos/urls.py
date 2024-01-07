from django.urls import path
from . import views


urlpatterns = [
    path("projetos/", views.projetos, name="projetos"),
]
