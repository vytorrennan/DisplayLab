from django.urls import path
from . import views


urlpatterns = [
    path("revista/", views.revista, name="revista"),
    path("revista/<slug:url>/", views.paginaDePost, name="paginaDePost"),
]