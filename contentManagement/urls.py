from django.urls import path
from . import views

urlpatterns = [
    path("", views.contentManagement, name="contentManagement"),
    path("novoProjeto/", views.novoProjeto, name="novoProjeto"),
]