from django.urls import path
from . import views

urlpatterns = [
    path("novoProjeto", views.novoProjeto, name="novoProjeto"),
]